"""
Run DashCast semi-persistently on a Chromecast while allowing other
Chromecast apps to work also by only launching when idle.
"""

from __future__ import print_function
import time
import os
import sys
import logging
import json
import paho.mqtt.client as mqtt

import pychromecast
import pychromecast.controllers.dashcast as dashcast


print('DashCast')
print('Searching for Chromecasts...')

DEFAULT_DASHBOARD_URL = os.getenv('DEFAULT_DASHBOARD_URL', 'https://home-assistant.io')
DEFAULT_DASHBOARD_URL_FORCE = os.getenv('DEFAULT_DASHBOARD_URL_FORCE') == 'True'
DISPLAY_NAME = os.getenv('DISPLAY_NAME')
IGNORE_CEC = os.getenv('IGNORE_CEC') == 'True'

SUBSCRIBE = 'chromecast/' + str(DISPLAY_NAME) + '/command/dashcast'
MQTT_SERVER = os.getenv('MQTT_SERVER', 'iot.eclipse.org')
MQTT_USERNAME = os.getenv('MQTT_USERNAME')
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD')

if IGNORE_CEC:
    print('Ignoring CEC for Chromecast', DISPLAY_NAME)
    pychromecast.IGNORE_CEC.append(DISPLAY_NAME)


if '--show-debug' in sys.argv:
    logging.basicConfig(level=logging.DEBUG)


class DashboardLauncher():

    def __init__(self, device, dashboard_url='https://home-assistant.io',
                 dashboard_url_force=False, dashboard_app_name='DashCast'):
        self.device = device
        print('DashboardLauncher', self.device.name)

        # register dashcast controller
        self.controller = dashcast.DashCastController()
        self.device.register_handler(self.controller)

        # Breaking Change pychromecast 3.0
        # Do not automatically start worker thread and connect in Chromecast constructor
        # https://github.com/balloob/pychromecast/pull/271
        self.device.wait()

        # register status listener
        receiver_controller = device.socket_client.receiver_controller
        receiver_controller.register_status_listener(self)

        # register connection listener
        self.device.socket_client.media_controller.register_status_listener(self)
        self.device.register_connection_listener(self)

        # set default url and dashboard app name
        self.dashboard_url = dashboard_url
        self.dashboard_url_force = dashboard_url_force
        self.dashboard_app_name = dashboard_app_name
        self.takeover = False

        # Check status on init.
        self.new_cast_status(self.device.status)
        # Launch dashboard on init.
        self.launch_dashboard(self.dashboard_url, self.dashboard_url_force)

        # While dashboard is launching, start MQTT connection
        print("Starting MQTT")
        client = mqtt.Client("client_" + str(DISPLAY_NAME))  # create new instance
        client.on_message = self.on_message  # attach function to callback
        client.on_connect = self.on_connect
        print("Connecting to Broker: " + MQTT_SERVER)
        client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        client.connect(MQTT_SERVER)  # connect to broker

        # wait for dashboard to finish loading, then start MQTT client loop
        time.sleep(10)
        client.loop_start()

        # keep_looping is the control variable.
        # If it is False, loop stops, program cleans up and exits
        self.keep_looping = True

        # if launch_it is set to true, the dashboard is relaunched
        # otherwise sleep a second and check again
        self.launch_it = False
        while self.keep_looping:
            if self.launch_it:
                print('launch_it', self.launch_it)
                self.launch_dashboard(self.dashboard_url, self.dashboard_url_force)
                self.launch_it = False
                time.sleep(10)
            time.sleep(1)

        client.loop_stop()

    # define MQTT client callbacks

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        print("Subscribing to topic ", SUBSCRIBE)
        client.subscribe(SUBSCRIBE)

    def on_message(self, client, userdata, message):
        print("Message received: ", str(message.payload.decode("utf-8")))
        print("-Topic: ", message.topic)
        print("-QOS: ", message.qos)
        print("-Retain: ", message.retain)

        # try decoding received message
        try:
            json_decode = str(message.payload.decode("utf-8", "ignore"))
            print("Decoding Json")
            parsed_json = json.loads(json_decode)
        except json.decoder.JSONDecodeError:
            print("Error passing JSON")
            return

        # set dashboard_url to received data and
        # set to relaunch/update dashboard
        print("Chromecast: " + DISPLAY_NAME)
        if 'url' in parsed_json:
            print("Url: " + parsed_json["url"])
            self.dashboard_url = parsed_json["url"]

            if 'force' in parsed_json:
                print("Force: " + str(parsed_json["force"]))
                self.dashboard_url_force = parsed_json["force"]
            else:
                self.dashboard_url_force = False

            if 'takeover' in parsed_json:
                print("Takeover: " + str(parsed_json["takeover"]))
                self.takeover = parsed_json["takeover"]
            else:
                self.takeover = False

            self.dashboard_url = parsed_json["url"]

            if self.is_dashboard_active() or self.takeover:
                self.launch_it = True

    # Define pychromecast Callback Receivers
    def new_cast_status(self, cast_status):
        """ Called when a new cast status has been received. """
        print('new_cast_status', self.device.name, cast_status)

        def should_launch():
            """ If the device is active, the dashboard is not already active, and no other app is active. """
            print('should launch', self.is_device_active(),
                  not self.is_dashboard_active(), not self.is_other_app_active())
            return (self.is_device_active()
                    and not self.is_dashboard_active()
                    and not self.is_other_app_active())

        if should_launch():
            self.launch_it = True

    def new_media_status(self, media_status):
        """Called when a new MediaStatus is received."""
        print('new_media_status', self.device.name, media_status)

    def new_connection_status(self, connection_status):
        """Called when a new ConnectionStatus is received."""
        print('new_connection_status', self.device.name, connection_status)

    def is_device_active(self):
        """ Returns if there is currently an app running and (maybe) visible. """

        return (self.device.status is not None
                #and self.device.app_id is not None
                and (self.device.status.is_active_input or self.device.ignore_cec)
                #and (not self.device.status.is_stand_by and not self.device.ignore_cec)
                )

    def is_dashboard_active(self):
        """ Returns if the dashboard is (probably) visible. """
        return self.device.app_display_name == self.dashboard_app_name

    def is_other_app_active(self):
        """ Returns if an app other than the dashboard or the Backdrop is (probably) visible. """
        return self.device.app_display_name not in ('Backdrop', self.dashboard_app_name)

    def launch_dashboard(self, url_to_load, force):
        print('Launching dashboard on Chromecast', self.device.name)

        def callback(response):
            print('callback called', response)

        try:
            self.controller.load_url(url_to_load, force, callback_function=callback)
        except Exception as e:
            print(e)
            pass


casts = pychromecast.get_chromecasts()
if len(casts) == 0:
    print('No Devices Found')
    exit()

for cc in casts:
    print('enumerate-casts', cc.device.friendly_name)

cast = next(cc for cc in casts if DISPLAY_NAME in (None, '') or cc.device.friendly_name == DISPLAY_NAME)

if not cast:
    print('Chromecast with name', DISPLAY_NAME, 'not found')
    exit()

DashboardLauncher(cast, dashboard_url=DEFAULT_DASHBOARD_URL, dashboard_url_force=DEFAULT_DASHBOARD_URL_FORCE)

# Keep running
while True:
    time.sleep(1)
