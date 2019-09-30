FROM python:3.6-alpine

WORKDIR /project

COPY ./project/requirements.txt ./

RUN pip install -r requirements.txt

COPY ./project .

#USER

#ENV FLASK_APP=app.py
#ENV FLASK_ENV=development
#
#EXPOSE 5000

#CMD [ "python", "app.py" ]

#ENTRYPOINT [ "flask", "run" ]

#CMD [ "flask", "run" ]
#CMD [ "--host=127.0.0.1" ]
