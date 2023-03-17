FROM nvidia/cuda:12.0.1-cudnn8-devel-ubuntu20.04

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
    libgl-dev \
    libmagickwand-dev \
    libopenmpi-dev \
    mpich \
    ocl-icd-libopencl1 \
    python3 \
    python3-dev \
    python3-pip\
    && apt-get clean autoclean \
    && apt-get autoremove -y

COPY requirements.txt /requirements.txt

# Installing numpy for pyhton's convolution
RUN pip3 install --no-cache-dir -r requirements.txt

# Adding nvidia to OpenCL's vendors list
RUN mkdir -p /etc/OpenCL/vendors && \
    echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

# Forcing sr to /home/ubuntu path
COPY sr /home/ubuntu/sr

# Adding sr to $PATH
ENV PATH /home/ubuntu/sr/bin:$PATH

WORKDIR /TP

CMD [ "bash" ]

