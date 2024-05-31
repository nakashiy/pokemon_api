FROM python:3.10

ARG USERNAME=nakashiy
ARG UID=1000
ARG GID=$UID

RUN groupadd -g $GID $USERNAME \
    && useradd -u $UID -g $GID -m -s /bin/bash $USERNAME

WORKDIR /work
COPY requirements.txt ./

RUN apt-get update -qq && apt-get install -y --no-install-recommends

RUN pip install -U pip \
    && pip install --no-cache-dir --upgrade -r requirements.txt

ENV TZ Asia/Tokyo
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja

CMD ["python3", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]

USER $USERNAME
