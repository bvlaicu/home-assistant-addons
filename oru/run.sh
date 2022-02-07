#!/bin/bash

CONFIG_PATH=/data/options.json

export EMAIL="$(jq --raw-output '.email' $CONFIG_PATH)"
export PASSWORD="$(jq --raw-output '.password' $CONFIG_PATH)"
export MFA_TYPE="$(jq --raw-output '.mfa_type' $CONFIG_PATH)"
export MFA_SECRET="$(jq --raw-output '.mfa_secret' $CONFIG_PATH)"
export ACCOUNT_UUID="$(jq --raw-output '.account_uuid' $CONFIG_PATH)"
export METER_NUMBER="$(jq --raw-output '.meter_number' $CONFIG_PATH)"
export ACCOUNT_NUMBER="$(jq --raw-output '.account_number' $CONFIG_PATH)"
export SITE="$(jq --raw-output '.site' $CONFIG_PATH)"
export MQTT_HOST="$(jq --raw-output '.mqtt_host' $CONFIG_PATH)"
export MQTT_USER="$(jq --raw-output '.mqtt_user' $CONFIG_PATH)"
export MQTT_PASS="$(jq --raw-output '.mqtt_password' $CONFIG_PATH)"

echo "Params:"
echo "EMAIL =" $EMAIL
echo "PASSWORD =" $(sed 's/^........../**********/' <<<$PASSWORD)
echo "MFA_TYPE =" $MFA_TYPE
echo "MFA_SECRET =" $(sed 's/^........../**********/' <<<$MFA_SECRET)
echo "ACCOUNT_UUID =" $ACCOUNT_UUID
echo "METER_NUMBER =" $METER_NUMBER
echo "ACCOUNT_NUMBER =" $ACCOUNT_NUMBER
echo "SITE =" $SITE
echo "MQTT_HOST =" $MQTT_HOST
echo "MQTT_USER =" $MQTT_USER
echo "MQTT_PASS =" $(sed 's/^........../**********/' <<<$MQTT_PASS)

# Start the listener and enter an endless loop
echo "Starting endless loop.."
while true; do 
  python3 run.py
  #tail -f /dev/null

  sleep 300
done