FROM python:3.11

WORKDIR /myapp

RUN apt-get update

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD "bash"