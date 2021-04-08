FROM python:3.9.4-buster

WORKDIR /app

COPY app/requirements.txt /app/

RUN pip install -r requirements.txt

COPY app /app

RUN ls -la

COPY entrypoint.sh ./
RUN chmod a+x entrypoint.sh

ENV FLASK_ENV=development

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["flask", "run", "--host=0.0.0.0"]
