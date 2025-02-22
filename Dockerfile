FROM  public.ecr.aws/docker/library/python:3.11.11-slim-bookworm AS build

RUN <<eot
    set -ex

    apt-get update
    apt install -y gcc
    useradd -ms /bin/bash tz
eot

USER tz

WORKDIR /home/tz

COPY --chown=tz:tz . .

RUN pip install --no-cache-dir --user .


FROM public.ecr.aws/docker/library/python:3.11.11-alpine

LABEL description="Get local datetime from multiple timezones!"

RUN <<eot
    set -ex

    apk update
    apk upgrade expat libuuid
    apk add --no-cache ncurses
    rm -rf /var/cache/apk/*
    addgroup -S tz
    adduser -S tz -u 1000
eot

USER tz

WORKDIR /home/tz

ENV PATH=$PATH:/home/tz/.local/bin

COPY --from=build --chown=tz /home/tz/.local /home/tz/.local/

ENTRYPOINT [ "tz" ]
