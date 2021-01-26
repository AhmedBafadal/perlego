FROM python:3.7.2-alpine3.9

MAINTAINER Ahmed Bafadal

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache python3-dev libstdc++ && \
    apk add --no-cache g++ && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    pip3 install numpy && \
    pip3 install pandas


COPY ./requirements.txt /requirements.txt


RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install -r /requirements.txt
RUN pip install --upgrade django-cors-headers
RUN apk del .tmp-build-deps


RUN mkdir /app

WORKDIR /app
COPY ./app /app





