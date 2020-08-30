FROM alpine:3.8

RUN apk add --no-cache \
        python3 \
        poppler-dev \
        libxslt-dev \
        postgresql-libs \
        build-base \
        jpeg-dev \
        zlib-dev

WORKDIR /psy_time

COPY requirements.txt /psy_time/

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=psy_time.prod \
    PORT=8000 \
    WEB_CONCURRENCY=3

EXPOSE 8000

RUN apk update && \
    apk add --no-cache --virtual .build-deps git build-base gcc python3-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk del --no-cache .build-deps

COPY . /psy_time

RUN python3 manage.py collectstatic --noinput --clear

CMD gunicorn psy_time.wsgi:application --bind 0.0.0.0:$PORT