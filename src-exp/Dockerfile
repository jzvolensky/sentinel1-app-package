FROM python:3.8-alpine

RUN apk update && \
    apk add --no-cache \
    ca-certificates \
    bash \
    wget


RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    /bin/bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh


ENV PATH="/opt/conda/bin:${PATH}"

COPY environment.yml /app/environment.yml
RUN conda env create -f /app/environment.yml && \
    conda clean -afy
ENV PATH="/opt/conda/envs/myenv/bin:${PATH}"

WORKDIR /app

COPY params.yaml /app
COPY hello_world.py /app

ENV PATH="/app:${PATH}"

CMD ["hello_world.py"]
