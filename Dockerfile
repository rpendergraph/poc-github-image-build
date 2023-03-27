FROM python:3.11-alpine3.16

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python main.py