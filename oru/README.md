# Orange and Rockland Utility to MQTT Bridge hass.io addon

Add-on for retrieving the last meter read from [Orange and Rockland Utility](oru.com) or [ConEdison](coned.com) and publish the data via MQTT

## Configuration

Add-on configuration example:

```yaml
email: example@email.com
password: '!secret oru_password'
mfa_type: TOTP
mfa_secret: '!secret oru_mfa_secret'
account_uuid: ef788d65-5380-11e8-8211-2655115779ac
meter_number: 706438804
site: oru
mqtt_host: hassio.local
mqtt_user: mqtt
mqtt_password: '!secret mqtt_password'
```
### Option: `email`

The email address for the oru.com / coned.com account

### Option: `password`

The password for the oru.com / coned.com account

### Option: `mfa_type`

The MFA type for the oru.com / coned.com account. Can be either `SECURITY_QUESTION` or `TOTP` (e.g. Google Authenticator).

### Option: `mfa_secret`

The MFA secret for the oru.com / coned.com account. For MFA type Security Question, to set up your MFA secret (answer), log into oru.com / coned.com, go to your profile and reset your 2FA method. When setting up 2FA again, there will be option to say you do not have texting on your phone. Select this and you should be able to use a security question instead.
For MFA type TOTP, choose Google Authenticator, choose a device type and when presented with the QR code, click on "Can't scan?". It should provide you with the MFA secret.

### Option: `account_uuid`

The Orange and Rockland Utility account uuid. To find it log into oru.com / coned.com then use the browser developer tools to search for `uuid` in the network tab. 

### Option: `meter_number`

The Orange and Rockland Utility meter number. You can find it on a utility bill.

### Option: `site`

Either `oru` for Orange and Rockland Utility or `coned` for ConEdison

### Option: `mqtt_host`

Defines the hostname or ip of the MQTT server

### Option: `mqtt_user`

Defines the username for the MQTT server

### Option: `mqtt_password`

Defines the password for the MQTT server


## MQTT Data

The addon will publish the latest meter read value and unit of measure to the following topics:

`electric_meter/startTime`

`electric_meter/endTime`

`electric_meter/value`

`electric_meter/uom`

## Home Assistant Energy

To enable tracking of your power usage with the new (as of 08/2021) Home Assistant Energy panel, you must add the following to your `configuration.yaml`:

```yaml

homeassistant:
  ...
  customize_glob:
    sensor.oru_energy_total_kwh:
      last_reset: "1970-01-01T00:00:00+00:00"
      device_class: energy
      state_class: measurement
      unit_of_measurement: "kWh"

sensor:
  ...
  - platform: mqtt
    name: "Oru Energy Usage"
    unique_id: "oru_energy"
    state_topic: "electric_meter/value"
    unit_of_measurement: "kWh"
    device_class: energy
    state_class: measurement
  - platform: statistics
    name: oru_energy_usage_stats
    entity_id: sensor.oru_energy_usage
  - platform: template
    sensors:
      oru_energy_total_kwh:
        friendly_name: Total ORU Energy
        device_class: energy
        value_template: "{{ state_attr('sensor.oru_energy_usage_stats', 'total') }}"
        unit_of_measurement: 'kWh'

```

*** Home Assistant Energy Monitoring Feature ***
To integrate the above setup with the new Home Assistant Energy Momitoring feature. simply add "Total ORU Energy" entity in the Energy Configuration page of your Home Assistant

<img width="1024" alt="Screen Shot 2021-08-24 at 4 40 01 PM" src="https://user-images.githubusercontent.com/15055127/130686826-7d94df43-dfe5-473b-adc2-1364cfb2ee25.png">

Wait for atleast 2-3 hours for the dashboard to populate, and it should look something like this:

<img width="1657" alt="Screen Shot 2021-08-24 at 4 24 37 PM" src="https://user-images.githubusercontent.com/15055127/130686905-b5597466-a945-4b98-b10d-7de56fc55885.png">
