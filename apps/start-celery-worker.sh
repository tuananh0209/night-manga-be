#!/bin/bash

cd /usr/src/apps
/usr/src/apps/virtualenv/bin/celery -A core worker -P eventlet -c 10
