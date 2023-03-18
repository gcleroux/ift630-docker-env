FROM ubuntu:20.04

LABEL author="Guillaume Cléroux"
LABEL email="guillaume.cleroux@usherbrooke.ca"
LABEL description="Un environnement de développement intégré avec docker pour le cours IFT630"

# Assign timezone for imagemagick
ENV TZ=America/Toronto
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Installing gcc and sr libs
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    clinfo \
    gcc-multilib \
    git \
    htop \
    imagemagick \
    intel-opencl-icd \
    libmagickwand-dev \
    libopenmpi-dev \
    mpich \
    python3 \
    python3-dev \
    python3-pip\
    && apt-get clean autoclean \
    && apt-get autoremove -y

COPY requirements.txt /requirements.txt

# Installing numpy for pyhton's convolution
RUN pip3 install --no-cache-dir -r requirements.txt

# Forcing sr to /home/ubuntu path
COPY sr /home/ubuntu/sr

# Adding sr to $PATH
ENV PATH /home/ubuntu/sr/bin:$PATH

# Allow MPI to run as root
ENV OMPI_ALLOW_RUN_AS_ROOT 1
ENV OMPI_ALLOW_RUN_AS_ROOT_CONFIRM 1

WORKDIR /TP

CMD [ "bash" ]

