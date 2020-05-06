FROM python:3.7-slim

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./containerizedproject .

ARG myVAR=QWERTYUIO
RUN echo $myVAR qwerty

#ENV qwe=123
#ENTRYPOINT ["python", "manage.py"]
##CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
