#!/bin/sh

export LANG=C
PATH="/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin"

echo "/usr/local/lib64/" > /etc/ld.so.conf
export LD_LIBRARY_PATH=/usr/local/lib64/
touch /var/log/rtl_433.log

CONFIG_PATH=/data/options.json
MQTT_HOST="$(jq --raw-output '.mqtt_host' $CONFIG_PATH)"
MQTT_USER="$(jq --raw-output '.mqtt_user' $CONFIG_PATH)"
MQTT_PASS="$(jq --raw-output '.mqtt_password' $CONFIG_PATH)"
MQTT_MSGTYPE="$(jq --raw-output '.msgType' $CONFIG_PATH)"
MQTT_IDS="$(jq --raw-output '.ids' $CONFIG_PATH)"


# Start the listener and enter an endless loop
echo "Starting RTLAMR with parameters:"
echo "MQTT Host =" $MQTT_HOST
echo "MQTT User =" $MQTT_USER
#MQTT_PASS_REDACTED=$(sed 's/^......./*******/' <<<$MQTT_PASS)
#echo "MQTT Password =" $MQTT_PASS_REDACTED
echo "MQTT Message Type =" $MQTT_MSGTYPE
echo "MQTT Device IDs =" $MQTT_IDS


#set -x  ## uncomment for MQTT logging...
/usr/local/bin/rtl_tcp &>/dev/null &

# Sleep to fill buffer a bit
sleep 15

LASTVAL="0"

# set a time to listen for. Set to 0 for unliminted

#tail -f /dev/null

# Do this loop, so will restart if buffer runs out
while true; do 

  ID_FILTER_OPTION=""
  if [ -z ${MQTT_IDS+x} ]; then 
    ID_FILTER_OPTION=""
  else 
    ID_FILTER_OPTION=$MQTT_IDS
  fi

  /go/bin/rtlamr -format json -msgtype=$MQTT_MSGTYPE $ID_FILTER_OPTION | while read line

  do
    VAL="$(echo $line | jq --raw-output '.Message.Consumption' | tr -s ' ' '_')" # replace ' ' with '_'
    DEVICEID="$(echo $line | jq --raw-output '.Message.ID' | tr -s ' ' '_')"
    MSGTYPE="$(echo $line | jq --raw-output '.Type' | tr -s ' ' '_')"
    MQTT_PATH="rtlamr/$DEVICEID/meter_reading"

    # Create file with touch /var/log/rtl_433.log if logging is needed
    [ -w /var/log/rtl_433.log ] && echo $line >> /var/log/rtl_433.log
    if [ "$VAL" != "$LASTVAL" ]; then
      echo $VAL | /usr/bin/mosquitto_pub -h $MQTT_HOST -u $MQTT_USER -P $MQTT_PASS -i RTL_433 -r -l -t $MQTT_PATH
    LASTVAL=$VAL
    fi
    
  done

  sleep 60

done