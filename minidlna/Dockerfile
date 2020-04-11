ARG BUILD_FROM=hassioaddons/base-amd64:1.2.0
FROM ${BUILD_FROM}

# Copy root filesystem
#COPY rootfs /

# Setup base
RUN apk add --no-cache minidlna

# Build arugments
ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_REF
ARG BUILD_VERSION

# Labels
LABEL \
    io.hass.name="MiniDLNA" \
    io.hass.description="RedyMedia MiniDLNA daemon serves media files (music, pictures, and video) to clients on a network" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="Bogdan Vlaicu <bogdanvlaicu@yahoo.com>" \
    org.label-schema.description="RedyMedia MiniDLNA daemon serves media files (music, pictures, and video) to clients on a network" \
    org.label-schema.build-date=${BUILD_DATE} \
    org.label-schema.name="MiniDLNA" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.url="https://addons.community" \
    org.label-schema.usage="https://github.com/bvlaicu/home-assistant-addons/tree/master/README.md" \
    org.label-schema.vcs-ref=${BUILD_REF} \
    org.label-schema.vcs-url="https://github.com/bvlaicu/addon-minidlna" \
    org.label-schema.vendor="Community Hass.io Addons"