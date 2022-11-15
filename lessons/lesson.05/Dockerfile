FROM python:3.8

ENV PYTHONBUFFERED=1
ENV DEBUG=1

WORKDIR /otus

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY otusblog .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
