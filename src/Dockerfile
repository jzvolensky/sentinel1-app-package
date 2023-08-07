# Use an Ubuntu base image
FROM ubuntu:latest

# Set the working directory
WORKDIR /app

# Update package lists and install necessary packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ca-certificates file wget bash bzip2 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Download and install Micromamba
RUN wget -qO- https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj bin/micromamba --strip-components=1 && \
    mv micromamba /usr/bin/

# Copy the conda environment file to the container
COPY environment.yml /app/environment.yml

# Create the conda environment
RUN micromamba create -f environment.yml

# Activate the conda environment
SHELL ["/bin/bash", "-c"]
RUN echo "source activate sen1grdenv" >> ~/.bashrc

# Copy your application code to the container
COPY . /app

# Run your application
CMD ["micromamba", "run", "-n", "sen1grdenv", "python", "app.py"]
