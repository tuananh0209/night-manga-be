FROM python:3.9

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# RUN apk add --update openssl && \
#     rm -rf /var/cache/apk/*

# # Install dependencies
# RUN \
#     apk add --no-cache postgresql-libs && \
#     apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
#     apk add --no-cache gettext gettext-dev libffi-dev zlib-dev jpeg-dev && \
#     apk add --no-cache python3-dev libffi-dev musl-dev make automake g++ subversion


# RUN openssl genrsa -out jwt_api_key 1024
# RUN openssl rsa -in jwt_api_key -pubout -out jwt_api_key.pub

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY /requirements.txt /requirements.txt
RUN pip install --upgrade pip
# RUN pip install --upgrade pip setuptools wheel
RUN pip install -r /requirements.txt --verbose
# RUN pip install opencv-python==4.5.3.56 --verbose

COPY ./apps/start-dev.sh /usr/src/apps/start-dev.sh
RUN chmod +x /usr/src/apps/start-dev.sh
COPY ./apps/start-dev.sh /start-services.sh
RUN chmod +x /start-services.sh
# RUN chmod +x /usr/src/apps/start-dev.sh

WORKDIR /usr/src/apps
