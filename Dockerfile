FROM ubuntu:20.04

LABEL author="Guillaume Cléroux"
LABEL email="guillaume.cleroux@usherbrooke.ca"
LABEL description="Un environnement de développement intégré avec \
docker pour le cours IFT630"

# Assign timezone for imagemagick
ENV TZ=America/Toronto
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Installing gcc and sr libs
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc-multilib \
    htop \
    python3 \
    python3-pip\
    imagemagick \
    libmagickwand-dev --no-install-recommends \
    clinfo \
    intel-opencl-icd \
    && apt-get clean autoclean \
    && apt-get autoremove -y

COPY requirements.txt /requirements.txt

# Installing numpy for pyhton's convolution
RUN pip3 install --no-cache-dir -r requirements.txt

# Forcing sr to /home/ubuntu path
COPY sr /home/ubuntu/sr

# Adding sr to $PATH
ENV PATH /home/ubuntu/sr/bin:$PATH

WORKDIR /TP

CMD [ "bash" ]
