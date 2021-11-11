FROM python:3.9.8-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY otusblog .

COPY prestart.sh /etc/prestart.sh
RUN chmod +x /etc/prestart.sh

ENTRYPOINT ["/etc/prestart.sh"]
CMD python manage.py runserver 0.0.0.0:8000
