#!/usr/bin/with-contenv bash
# ==============================================================================
# Community Hass.io Add-ons: torrdlna
# Ensures necessary mounting is done
# ==============================================================================
# shellcheck disable=SC1091
source /usr/lib/hassio-addons/base.sh

if ! grep -qs '/share/hdd' /proc/mounts; then
    mount /dev/sda1 /share/hdd || hass.die 'Could not mount hdd'
fi
