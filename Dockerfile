#BASE
FROM python:3.7-alpine

#log
ENV PYTHONUNBUFFERD 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# update pip
# RUN pip install --upgrade pip

RUN mkdir /django-api
WORKDIR /django-api

COPY ./django-api /django-api

RUN adduser -D user
USER user
