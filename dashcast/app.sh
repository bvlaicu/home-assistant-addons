#!/bin/bash

CONFIG_PATH=/data/options.json

DISPLAY_NAME=$(jq --raw-output '.chromecast_name // empty' $CONFIG_PATH)
echo "DISPLAY_NAME=${DISPLAY_NAME}"
export DISPLAY_NAME

DEFAULT_DASHBOARD_URL=$(jq --raw-output '.dashboard_url // empty' $CONFIG_PATH)
echo "DEFAULT_DASHBOARD_URL=${DEFAULT_DASHBOARD_URL}"
export DEFAULT_DASHBOARD_URL

MQTT_SERVER=$(jq --raw-output '.mqtt_host // empty' $CONFIG_PATH)
echo "MQTT_SERVER=${MQTT_SERVER}"
export MQTT_SERVER

MQTT_USERNAME=$(jq --raw-output '.mqtt_user // empty' $CONFIG_PATH)
echo "MQTT_USERNAME=${MQTT_USERNAME}"
export MQTT_USERNAME

MQTT_PASSWORD=$(jq --raw-output '.mqtt_pass // empty' $CONFIG_PATH)
echo "MQTT_PASSWORD=${MQTT_PASSWORD}"
export MQTT_PASSWORD

# Keep the python app alive.
while true; do python -u app_mqtt.py --show-debug; done
