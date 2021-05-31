# set base image (host OS)
FROM python:3.8

ADD receive.py /

RUN pip install pika

CMD [ "python", "./receive.py" ]
