# This Dockerfile will only work with host networking enabled.

# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

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
