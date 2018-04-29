# fail on run xdummy (doesn't have permision)
# FROM continuumio/anaconda3:latest

# TODO: has python2. should install python 3
# FROM ubuntu:latest

FROM python:3.6

RUN apt-get update && \
    apt-get install -y libav-tools \
    python-numpy \
    python-scipy \
    python-pyglet \
    python-setuptools \
    libpq-dev \
    libjpeg-dev \
    curl \
    cmake \
    swig \
    freeglut3 \
    python-opengl \
    libboost-all-dev \
    libglu1-mesa \
    libglu1-mesa-dev \
    libsdl2-2.0-0\
    libgles2-mesa-dev \
    libsdl2-dev \
    wget \
    unzip \
    git \
    xserver-xorg-input-void \
    xserver-xorg-video-dummy \
    python-gtkglext1 \
    xpra \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && easy_install pip


# install ffmpeg
# It is now available for Jessy as a backport: https://packages.debian.org/jessie-backports/ffmpeg
RUN echo "deb http://ftp.uk.debian.org/debian jessie-backports main" >> /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/gym
#RUN mkdir -p gym && touch gym/__init__.py
#COPY ./gym/version.py ./gym
#COPY ./requirements.txt .
#COPY ./setup.py .
RUN pip install gym[atari,box2d,classic_control]

COPY requirements.txt /usr/local/gym
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

# Finally, upload our actual code!
COPY . /usr/local/gym

#WORKDIR /root
WORKDIR /usr/local/gym
ENTRYPOINT ["/usr/local/gym/bin/docker_entrypoint"]
