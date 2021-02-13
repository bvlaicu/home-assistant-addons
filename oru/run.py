import os
import asyncio
from coned import Meter
from coned import MeterError
import paho.mqtt.client as mqtt
import json

meter = Meter(
    email=os.getenv("EMAIL"),
    password=os.getenv("PASSWORD"),
    mfa_type=os.getenv("MFA_TYPE"),
    mfa_secret=os.getenv("MFA_SECRET"),
    account_uuid=os.getenv("ACCOUNT_UUID"),
    meter_number=os.getenv("METER_NUMBER"),
    site=os.getenv("SITE"),
    browser_path="/usr/bin/google-chrome-stable"
)
startTime, endTime, value, uom = asyncio.get_event_loop().run_until_complete(meter.last_read())

message = {'startTime': startTime, 'endTime': endTime, 'value': value, 'uom': uom}

print(f"message: {message}")

mqttc = mqtt.Client("oru_meter_reader")
mqttc.username_pw_set(username=os.getenv("MQTT_USER"), password=os.getenv("MQTT_PASS"))
mqttc.connect(os.getenv("MQTT_HOST"))
mqttc.publish('electric_meter/startTime', startTime, retain=True)
mqttc.publish('electric_meter/endTime', endTime, retain=True)
mqttc.publish('electric_meter/value', value, retain=True)
mqttc.publish('electric_meter/uom', uom, retain=True)
mqttc.publish('electric_meter/message', json.dumps(message), retain=True)
mqttc.disconnect()
