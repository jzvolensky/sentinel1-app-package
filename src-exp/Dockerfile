# Use a smaller base image
FROM python:3.8-alpine

# Update the package index and install required packages
RUN apk update && \
    apk add --no-cache \
    ca-certificates \
    bash \
    wget

# Download and install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    /bin/bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh

# Set the PATH environment variable
ENV PATH="/opt/conda/bin:${PATH}"

# Copy environment.yml and create Conda environment
COPY environment.yml /app/environment.yml
RUN conda env create -f /app/environment.yml && \
    conda clean -afy

# Set the PATH environment variable for the Conda environment
ENV PATH="/opt/conda/envs/myenv/bin:${PATH}"

# Set the working directory
WORKDIR /app

# Copy files into the container
COPY params.yaml /app
COPY hello_world.py /app

# Update the PATH environment variable
ENV PATH="/app:${PATH}"

# Set the command to run when the container starts
CMD ["hello_world.py"]
