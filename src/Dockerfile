# Use official Python image (Alpine)
FROM python:3.11.0-alpine

WORKDIR /usr/src/app

# Prevent Python from writing .pyc files and buffer output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy requirements early to cache dependencies
COPY requirements.txt /usr/src/app/requirements.txt

# Install dependencies & build dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
         openssl-dev libffi-dev gcc musl-dev python3-dev \
         postgresql-dev bash \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/app/requirements.txt \
    && rm -rf /root/.cache/pip

# Copy the rest of the code
COPY . /usr/src/app/
