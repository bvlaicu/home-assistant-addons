#!/usr/bin/with-contenv bash
# ==============================================================================
# Community Hass.io Add-ons: torrdlna
# Ensures necessary directories exists
# ==============================================================================
# shellcheck disable=SC1091
source /usr/lib/hassio-addons/base.sh

if ! hass.directory_exists '/share/hdd/incomplete'; then
    mkdir -p /share/hdd/incomplete || hass.die 'Could not create hdd torrents incomplete directory'
    chmod -R 0777 /share/hdd/incomplete
fi
