FROM ubuntu

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ca-certificates file wget bash bzip2 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh

COPY environment.yml /app/environment.yml

ENV PATH="/opt/conda/bin:${PATH}"

RUN conda env create -f /app/environment.yml && \
    conda clean -afy
ENV PATH="/opt/conda/envs/myenv/bin:${PATH}"

WORKDIR /app

COPY /params.yaml /app

COPY ./hello_world.py /app

ENV PATH="/app:${PATH}"