#FROM python:3.9-buster
FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV FLASK_ENV=production

COPY ./requirements.txt requirements.txt

RUN pip install -U pip

RUN pip install -r requirements.txt

COPY . .
