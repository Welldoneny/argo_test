FROM python:3.11-slim

RUN pip install redis
RUN pip install flask
ADD server.py /server/

WORKDIR /server/