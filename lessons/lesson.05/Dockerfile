FROM python:3.9.12-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY otusblog .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
