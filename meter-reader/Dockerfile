ARG BUILD_FROM
FROM $BUILD_FROM

# Add env
ENV LANG C.UTF-8

RUN apk add --no-cache curl
RUN apk add --no-cache python3
RUN apk add --no-cache nano

RUN apk add cmd:pip3

# install .py script dependency
RUN pip3 install boto3
RUN pip3 install requests
RUN pip3 install paho-mqtt

# Copy data for add-on
COPY ocr_aws.py /
COPY run.sh /

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
