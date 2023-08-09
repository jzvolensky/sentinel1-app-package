FROM ubuntu:latest

WORKDIR /app

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ca-certificates file wget bash bzip2 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN wget -qO- https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj bin/micromamba --strip-components=1 && \
    mv micromamba /usr/bin/

COPY environment.yml /app/environment.yml

RUN micromamba create -f environment.yml

SHELL ["/bin/bash", "-c"]
RUN echo "source activate sen1env" >> ~/.bashrc

COPY . /app

CMD ["micromamba", "run", "-n", "sen1env", "python", "app.py"]
