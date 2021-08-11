FROM debian:buster

USER root
RUN apt-get update && apt-get upgrade -yq
RUN apt-get install python3 python3-pip jq nano -y

# Install chromium
RUN apt-get update && apt-get install -y chromium
RUN ln -s /usr/bin/chromium /usr/bin/chromium-browser

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY run.py .
COPY run.sh .

CMD cd / && chmod +x /run.sh && /run.sh
