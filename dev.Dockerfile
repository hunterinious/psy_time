FROM alpine:3.8

RUN apk add --no-cache \
        python3 \
        poppler-dev \
        libxslt-dev \
        postgresql-libs \
        build-base \
        jpeg-dev \
        zlib-dev

COPY . /psy_time
WORKDIR /psy_time

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=psy_time.dev \
    PORT=8000

RUN apk update && \
    apk add --no-cache --virtual .build-deps git build-base gcc python3-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk del --no-cache .build-deps

EXPOSE 8000
