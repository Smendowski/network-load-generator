FROM bitnami/minideb

LABEL maintainer="Mateusz Smendowski"
LABEL version="1.0"

RUN apt-get update && \
    apt-get install -y procps && \
    apt-get install -y iperf && \
    apt-get clean && \ 
    addgroup iperf-users && \ 
    adduser --no-create-home --disabled-password --ingroup iperf-users iperf-server

ARG IPERF_SERVER_INSTANCE_PORT

USER iperf-server

ENTRYPOINT [ "/usr/bin/iperf" ]
CMD [ "-s" ]

EXPOSE ${IPERF_SERVER_INSTANCE_PORT}:${IPERF_SERVER_INSTANCE_PORT}