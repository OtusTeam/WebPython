FROM tiangolo/uwsgi-nginx-flask:python3.10

COPY ./app/requirements.txt /app/requirements.txt

RUN pip install -U pip && \
    pip install -r requirements.txt

COPY ./app /app
