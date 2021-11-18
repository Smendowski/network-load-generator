FROM telegraf

LABEL maintainer="Mateusz Smendowski"
LABEL version="1.0"

RUN apt-get update && \
    apt-get install -y iperf && \
    apt-get clean && \ 
    addgroup iperf-users && \ 
    adduser --no-create-home --disabled-password --ingroup iperf-users telegraf-iperf-client

ARG IPERF_CLIENT_INSTANCE_PORT

USER telegraf-iperf-client

EXPOSE ${IPERF_CLIENT_INSTANCE_PORT}:${IPERF_CLIENT_INSTANCE_PORT}