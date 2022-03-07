FROM python:3.9.2-slim-buster

ARG USER_UID=1000

RUN apt-get update \
    && apt-get install -y python3-pip\
    && pip3 install awsiotsdk\
    && pip3 install python-dotenv

RUN useradd -m -s /bin/bash -u $USER_UID runner\
    && mkdir -p /app\
    && chown -R runner:runner /app

ADD . /app

VOLUME /app
WORKDIR /app

USER runner

