FROM python:3.9-alpine

ENV MODE=${MODE}

WORKDIR /code
COPY ./requirements /code/requirements/

RUN mkdir -p /root/.config/pip
COPY pip.conf /root/.config/pip/pip.conf

COPY ./ /code/
RUN apk add --no-cache --upgrade --virtual .build-deps \
    gcc \
    linux-headers \
    mariadb-client \
    musl-dev \
    mariadb-connector-c-dev \
    && pip3.9 install -U pip setuptools \
    && pip install --no-cache-dir -r requirements/requirements.txt; \
    apk del --no-cache .build-deps \
    && apk add musl mariadb-connector-c

RUN apk add bash pcre mariadb-connector-c-dev
RUN adduser -D -u 1000 -G www-data uwsgi
EXPOSE 9999

USER uwsgi
CMD ["bash", "scripts/start_server.sh"]
