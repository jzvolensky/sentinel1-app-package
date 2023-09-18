FROM continuumio/miniconda3:latest

WORKDIR /app
COPY params.yaml /app
COPY hello_world.py /app
COPY environment.yml /app

RUN conda env create -f environment.yml

ENV PATH="/opt/conda/envs/myenv/bin:${PATH}"

CMD ["conda", "run", "-n", "ap-hello-world", "python", "hello_world.py"]
