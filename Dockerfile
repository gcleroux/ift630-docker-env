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
    build-essential=12.8ubuntu1 \
    gcc-multilib=4:9.3.0-1ubuntu2 \
    htop=2.2.0-2build1 \
    python3=3.8.2-0ubuntu2 \
    python3-pip=20.0.2-5ubuntu1.7 \
    imagemagick=8:6.9.10.23+dfsg-2.1ubuntu11.4 \
    libmagickwand-dev=8:6.9.10.23+dfsg-2.1ubuntu11.4 --no-install-recommends \
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
