FROM python:3.7.7

# set work directory
WORKDIR /usr/src/app

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x entrypoint.sh

# copy project
COPY ./myproj .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
