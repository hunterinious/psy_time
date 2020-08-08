FROM alpine:3.8

RUN apk add --no-cache \
        python3 \
        poppler-dev \
        libxslt-dev \
        postgresql-libs \
        build-base \
        jpeg-dev \
        zlib-dev

COPY . /src
WORKDIR /src

RUN apk update && \
    apk add --no-cache --virtual .build-deps git build-base gcc python3-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk del --no-cache .build-deps

EXPOSE 8000
