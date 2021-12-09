# BASE / no use alpine
FROM python:3

# log
ENV PYTHONUNBUFFERD 1

RUN mkdir /api-components
WORKDIR /api-components

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./api-components /api-components
