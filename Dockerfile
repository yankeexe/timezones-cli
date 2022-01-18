FROM python:3.9-slim-buster as build

RUN useradd -ms /bin/bash tz

USER tz

WORKDIR /home/tz

COPY --chown=tz:tz . .

RUN python setup.py bdist_wheel


FROM python:3.9-alpine

LABEL description="Get local datetime from multiple timezones!"

RUN apk update && apk add ncurses && \
    addgroup -S tz && adduser -S tz -u 1000

USER tz

WORKDIR /home/tz

ENV PATH=$PATH:/home/tz/.local/bin

COPY --from=build --chown=tz /home/tz/dist /home/tz/dist/

RUN pip install --no-cache-dir --user dist/*.whl

ENTRYPOINT [ "tz" ]
