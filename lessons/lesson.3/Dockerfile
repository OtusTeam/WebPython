FROM python:3.7.7-slim

WORKDIR /app

COPY project/requirements.txt .
RUN pip install -r requirements.txt

COPY project/* ./

#ENV FLASK_APP=app.py

EXPOSE 5000

#ARG SOME_ARG
#RUN echo Arg is $SOME_ARG

#ENTRYPOINT ["flask", "run"]
#CMD ["--host=0.0.0.0"]
