FROM  public.ecr.aws/docker/library/python:3.11.11-slim-bookworm AS build

ENV UV_PROJECT_ENVIRONMENT=/home/tz/.venv
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

RUN <<eot
    set -ex

    apt-get update
    apt install -y gcc
    useradd -ms /bin/bash tz
eot

USER tz

WORKDIR /home/tz

COPY --chown=tz:tz . .

COPY --from=ghcr.io/astral-sh/uv:0.6.2 /uv /bin/

RUN <<eot
    set -ex

    uv sync --frozen --no-dev --no-editable
eot

FROM public.ecr.aws/docker/library/python:3.11.11-alpine

LABEL description="Get local datetime from multiple timezones!"

ENV PATH="/home/tz/.venv/bin:/home/tz/.local/bin:$PATH"

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

COPY --from=build --chown=tz:tz /home/tz/.venv /home/tz/.venv

ENTRYPOINT [ "tz" ]
