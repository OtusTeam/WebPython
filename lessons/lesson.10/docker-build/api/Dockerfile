#FROM tiangolo/meinheld-gunicorn-flask:python3.9
FROM tiangolo/uwsgi-nginx-flask:python3.9

ENV PYTHONBUFFERED=1

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN pip install "greenlet<0.4.17"

COPY . .
