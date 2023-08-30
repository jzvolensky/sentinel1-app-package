FROM ubuntu

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ca-certificates file wget bash bzip2 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY /params.yaml /app

COPY ./hello_world.py /app

ENV PATH="/app:${PATH}"