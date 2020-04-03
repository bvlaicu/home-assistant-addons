#!/bin/bash

CONFIG_PATH=/data/options.json

DEFAULT_DASHBOARD_URL=$(jq --raw-output '.dashboard_url // empty' $CONFIG_PATH)

echo "DEFAULT_DASHBOARD_URL=${DEFAULT_DASHBOARD_URL}"

export DEFAULT_DASHBOARD_URL

# Keep the python app alive.
while true; do python -u app_mqtt.py --show-debug; done
