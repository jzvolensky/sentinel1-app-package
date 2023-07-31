FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]

ENV BASH_ENV=~/.bashrc                                                                                                      \
    MAMBA_ROOT_PREFIX=/srv/conda                                                                                            \
    PATH=$PATH:/srv/conda/envs/sen1grdenv/bin


WORKDIR /testing_folder

ADD environment.yml /testing_folder/tmp/environment.yml
COPY . /tmp

ADD app.py .

COPY params.yml /testing_folder/params.yml

RUN apt-get update                                                                                                          && \
    apt-get install -y ca-certificates ttf-dejavu file wget bash bzip2                                                      && \
    wget -qO- https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj bin/micromamba --strip-components=1 && \
    ./micromamba shell init -s bash -p ~/micromamba                                                                         && \
    apt-get clean autoremove --yes                                                                                          && \
    rm -rf /var/lib/{apt,dpkg,cache,log}                                                                                    && \
    cp ./micromamba /usr/bin                                                                                                && \
    micromamba create -f /tmp/environment.yml                                                                               && \
    conda activate sen1grdenv                                                                                                                                                                                        


