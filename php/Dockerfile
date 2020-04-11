#ARG BUILD_FROM=hassioaddons/base:7.0.2
## hadolint ignore=DL3006
#FROM ${BUILD_FROM}

FROM php:7.2-apache
RUN apt-get update && apt-get install -y curl wget

# Copy root filesystem
#COPY rootfs /

# Change docroot to /data
RUN sed -ri -e 's!/var/www/html!/data!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!/data!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

# Setup base
#RUN apk add --no-cache \
#    coreutils=8.31-r0 \
#    wget=1.20.3-r0

# Build arguments
ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_REF
ARG BUILD_VERSION

# Labels
LABEL \
    io.hass.name="PHP" \
    io.hass.description="PHP add-on for Home Assistant" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="Bogdan Vlaicu <bogdanvlaicu@yahoo.com>" \
    org.label-schema.description="PHP add-on for Home Assistant" \
    org.label-schema.build-date=${BUILD_DATE} \
    org.label-schema.name="PHP" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.url="https://addons.community" \
    org.label-schema.usage="https://github.com/bvlaicu/home-assistant-addons/blob/master/php/README.md" \
    org.label-schema.vcs-ref=${BUILD_REF} \
    org.label-schema.vcs-url="https://github.com/bvlaicu/home-assistant-addons/blob/master/php/" \
    org.label-schema.vendor="Community Hass.io Addons"
