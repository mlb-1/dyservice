#!/usr/bin/env bash

GUNICORN_WORKERS=${GUNICORN_WORKERS:-"5"}
GUNICORN_WORKER_CLASS=${GUNICORN_WORKER_CLASS:-"gevent"}
GUNICORN_WORKER_CONNECTIONS=${GUNICORN_WORKER_CONNECTIONS:-"2000"}
GUNICORN_BACKLOG=${GUNICORN_BACKLOG:-"1000"}


# Needed to allow utf8 use in the Monasca API
export PYTHONIOENCODING=utf-8
gunicorn --capture-output \
  -n dyservice \
  --worker-class="$GUNICORN_WORKER_CLASS" \
  --worker-connections="$GUNICORN_WORKER_CONNECTIONS" \
  --backlog=$GUNICORN_BACKLOG \
  --paste /etc/dyservice/api-config.ini \
  -w "$GUNICORN_WORKERS"
