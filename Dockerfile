FROM python:3.6

ENV PYTHONUNBUFFERED 1

ADD . /test_project
WORKDIR /test_project
