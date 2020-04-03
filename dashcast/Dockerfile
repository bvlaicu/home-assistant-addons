# This Dockerfile will only work with host networking enabled.

# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y curl wget nano jq

RUN curl -J -L -o /tmp/bashio.tar.gz \
        "https://github.com/hassio-addons/bashio/archive/v0.9.0.tar.gz" \
    && mkdir /tmp/bashio \
    && tar zxvf \
        /tmp/bashio.tar.gz \
        --strip 1 -C /tmp/bashio \
    \
    && mv /tmp/bashio/lib /usr/lib/bashio \
    && ln -s /usr/lib/bashio/bashio /usr/bin/bashio

# Define environment variables
ENV DEFAULT_DASHBOARD_URL "https://darksky.net"
ENV DEFAULT_DASHBOARD_URL_FORCE "False"
ENV DISPLAY_NAME ""
ENV IGNORE_CEC "True"

ENV MQTT_SERVER "iot.eclipse.org"
ENV MQTT_USERNAME ""
ENV MQTT_PASSWORD ""

# Run app.sh when the container launches
CMD ["./app.sh"]
