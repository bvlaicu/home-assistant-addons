#!/usr/bin/with-contenv bash
# ==============================================================================
# Community Hass.io Add-ons: torrdlna
# Ensures necessary directories exists
# ==============================================================================
# shellcheck disable=SC1091
source /usr/lib/hassio-addons/base.sh

if ! hass.directory_exists '/share/hdd'; then
    mkdir -p /share/hdd || hass.die 'Could not create hdd mount directory'
    chmod -R 0777 /share/hdd
fi
