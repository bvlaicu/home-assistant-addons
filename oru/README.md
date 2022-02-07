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
account_number: 004352784609234
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

The Orange and Rockland Utility account uuid. To find it log into oru.com then use the browser developer tools & follow the steps below;

Login to your account and go to
-> Home Page
-> Billing and Usage
-> Your Billing and Usage
-> Real Time usage
-> In browser developer tools, search for URL like : ```https://oru.opower.com/ei/edge/apis/cws-real-time-ami-v1/cws/oru/accounts/<YOUR_ACCOUNT_UUID>/meters/<YOUR_METER_NUMBER>/usage```

Copy your UUID from the URl and paste it in this config

### Option: `meter_number`

The Orange and Rockland Utility meter number. You can find it on a utility bill.

### Option: `account_number`

Optional – use only if you have more than one service address associated with your account. You can find it in the URL after logging in and navigating to the account, ex. `https://www.coned.com/en/accounts-billing/dashboard?account=004352784609234`

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
    sensor.*_energy:
      last_reset: '1970-01-01T00:00:00+00:00'
      device_class: energy
      state_class: measurement

sensor:
  ...
  - platform: mqtt
    name: "ConEd Energy Usage"
    unique_id: "coned_energy"
    state_topic: "electric_meter/value"
    unit_of_measurement: 'kWh'
    device_class: energy
    state_class: measurement

```
