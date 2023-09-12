FROM continuumio/miniconda3:latest

WORKDIR /app
COPY params.yaml /app
COPY hello_world.py /app
COPY environment.yml /app

RUN conda env create -f /app/environment.yml

ENV PATH="/opt/conda/envs/myenv/bin:${PATH}"

CMD ["/bin/bash","-c", "conda run -n ap-hello-world python hello_world.py"]
