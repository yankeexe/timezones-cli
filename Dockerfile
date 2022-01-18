FROM python:3.9-slim-buster

LABEL description="Get local datetime from multiple timezones!"

RUN useradd -ms /bin/bash timekeeper

USER timekeeper

WORKDIR /home/timekeeper

ENV PATH=$PATH:/home/timekeeper/.local/bin

RUN pip install --upgrade pip && \
    pip install --upgrade --user --no-cache-dir timezones-cli

ENTRYPOINT [ "tz" ]
