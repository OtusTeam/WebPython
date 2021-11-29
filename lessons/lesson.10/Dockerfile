FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY prestart.sh /etc/prestart.sh
RUN chmod +x /etc/prestart.sh

COPY . .

ENTRYPOINT ["/etc/prestart.sh"]

CMD python app.py
