FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get -y install cron
RUN mkdir /service
WORKDIR /service
ADD . /service/
RUN pip install -r requirements.txt
RUN touch /var/log/cron.log
RUN crontab cron.sh
