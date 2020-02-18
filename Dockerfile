FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /service
WORKDIR /service
ADD . /service/
RUN pip install -r requirements.txt
