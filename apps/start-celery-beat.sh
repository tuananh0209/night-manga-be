#!/bin/bash

cd /usr/src/apps
/usr/src/apps/virtualenv/bin/celery -A core beat
