import os
import asyncio
from coned import Meter
from coned import MeterError
import paho.mqtt.client as mqtt
import json
import logging
import time

print(f"Creating Meter")

meter = Meter(
    email=os.getenv("EMAIL"),
    password=os.getenv("PASSWORD"),
    mfa_type=os.getenv("MFA_TYPE"),
    mfa_secret=os.getenv("MFA_SECRET"),
    account_uuid=os.getenv("ACCOUNT_UUID"),
    meter_number=os.getenv("METER_NUMBER"),
    site=os.getenv("SITE"),
    browser_path="/usr/bin/chromium-browser"
    # browser_path="/usr/bin/google-chrome-stable"
)
# meter._LOGGER.setLevel(logging.DEBUG)

print(f"Calling meter.last_read()..")
startTime, endTime, value, uom = asyncio.get_event_loop().run_until_complete(meter.last_read())

message = {'startTime': startTime, 'endTime': endTime, 'value': value, 'uom': uom}

print(f"message: {message}")

mqtthost = os.getenv("MQTT_HOST")
mqttuser = os.getenv("MQTT_USER")
mqttpass = os.getenv("MQTT_PASS")

print(f"Connecting to mqtt {mqtthost} as {mqttuser}")

mqttc = mqtt.Client("oru_meter_reader")
mqttc.username_pw_set(username=mqttuser, password=mqttpass)
mqttc.connect(mqtthost)

print(f"Publishing to mqtt")

print(f"Publishing electric_meter/value: {value}")
mqttc.publish('electric_meter/value', value, retain=True)
time.sleep(1)

print(f"Publishing electric_meter/uom: {uom}")
mqttc.publish('electric_meter/uom', uom, retain=True)
time.sleep(1)

print(f"Publishing electric_meter/startTime: {startTime}")
mqttc.publish('electric_meter/startTime', startTime, retain=True)
time.sleep(1)

print(f"Publishing electric_meter/endTime: {endTime}")
mqttc.publish('electric_meter/endTime', endTime, retain=True)
time.sleep(1)

print(f"Publishing electric_meter/message: {json.dumps(message)}")
mqttc.publish('electric_meter/message', json.dumps(message), retain=True)
time.sleep(1)

print(f"Disconnectig from mqtt")
mqttc.disconnect()

print(f"DONE\n\n")
