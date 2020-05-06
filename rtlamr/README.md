# RTLAMR to MQTT Bridge hass.io addon
Add-on for software defined radio tuned to listen for 433MHz RF transmissions and republish the data via MQTT

This addon is based on the addon from jdeath here: https://github.com/jdeath/RTLAMR2MQQT
which is based on biochemguy's (non-docker) setup: https://community.home-assistant.io/t/get-your-smart-electric-water-and-gas-meter-scm-readings-into-home-assistant-with-a-rtl-sdr
which in turn is based on James Fry' project here: https://github.com/james-fry/hassio-addons/tree/master/rtl4332mqtt
which was based on Chris Kacerguis' project here: https://github.com/chriskacerguis/honeywell2mqtt,
which is in turn based on Marco Verleun's rtl2mqtt image here: https://github.com/roflmao/rtl2mqtt

## Configuration

Add-on configuration example:

```yaml
mqtt_host: hassio.local
mqtt_user: mqtt
mqtt_password: '!secret mqtt_password'
msg_type: all
meter_ids: '1487813232,15527764'
```

### Option: `mqtt_host`

The `mqtt_host` option defines the hostname or ip of the MQTT server

### Option: `mqtt_user`

The `mqtt_user` option defines the username for the MQTT server

### Option: `mqtt_password`

The `mqtt_password` option defines the password for the MQTT server

### Option: `msg_type`

The `msg_type` option defines the comma-separated list of message types to receive all, scm, scm+, idm, netidm, r900 and r900bcd

Default value: all

### Option: `meter_ids`

The `meter_ids` option defines the comma-separated list of meter ids to be processed

Optional. If not provided, all found meters will be processed

## MQTT Data

Topic: rtlamr/<METER_ID>/reading

## Hardware

This add-on has been tested and used with the following hardware

- NooElec NESDR Nano 2+ Tiny Black RTL-SDR USB
