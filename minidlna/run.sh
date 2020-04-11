#!/bin/bash

set -e

> /etc/minidlna.conf

for VAR in `env`; do
    if [[ $VAR =~ ^MINIDLNA_ ]]; then
        minidlna_name=`echo "$VAR" | sed -r "s/MINIDLNA_(.*)=.*/\1/g" | tr '[:upper:]' '[:lower:]'`
        minidlna_value=`echo "$VAR" | sed -r "s/.*=(.*)/\1/g"`
        echo "${minidlna_name}=${minidlna_value}" >> /etc/minidlna.conf
    fi
done

exec /usr/bin/minidlna -d $@