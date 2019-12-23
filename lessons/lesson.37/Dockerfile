FROM python:3.6-alpine

WORKDIR /project

COPY ./project/requirements.txt .

RUN pip install -r requirements.txt

COPY ./project/* ./

#EXPOSE 5000

#ARG VARIABLE="127.0.0.1"
#RUN echo VARIABLE is $VARIABLE

#ENTRYPOINT

#ENV HOST="127.0.0.1"

#ENV FLASK_APP=app.py
#CMD ["flask", "run", "--host=0.0.0.0"]
#ENTRYPOINT ["flask", "run"]
#CMD ["--host=0.0.0.0"]
#

#ENTRYPOINT ["python", "app.py"]
#ENTRYPOINT ["python"]
#CMD ["app.py"]
#CMD ["python", "app.py"]
