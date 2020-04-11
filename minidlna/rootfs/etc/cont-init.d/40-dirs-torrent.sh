#!/usr/bin/with-contenv bash
# ==============================================================================
# Community Hass.io Add-ons: torrdlna
# Ensures necessary directories exists
# ==============================================================================
# shellcheck disable=SC1091
source /usr/lib/hassio-addons/base.sh

if ! hass.directory_exists '/share/hdd/torrents'; then
    mkdir -p /share/hdd/torrents || hass.die 'Could not create hdd torrents directory'
    chmod -R 0777 /share/hdd/torrents
fi
