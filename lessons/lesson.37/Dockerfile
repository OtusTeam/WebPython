FROM python:3.7.8

WORKDIR /app

COPY project/requirements.txt .
RUN pip install -r requirements.txt

COPY project .

ENV FLASK_APP=app
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
