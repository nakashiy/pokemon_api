FROM python:3.10

ARG USERNAME=nakashiy
ARG UID=1000
ARG GID=$UID

RUN groupadd -g $GID $USERNAME \
    && useradd -u $UID -g $GID -m -s /bin/bash $USERNAME

RUN apt update -qq && apt install -y --no-install-recommends \
    sudo wget curl vim git tzdata locales && locale-gen ja_JP.UTF-8

RUN pip install --upgrade pip && \
    pip install opensearch-py pydantic

ENV TZ Asia/Tokyo
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja

USER $USERNAME
WORKDIR /work
