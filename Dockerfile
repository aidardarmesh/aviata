FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /service
WORKDIR /service
ADD . /service/
RUN pip install -r requirements.txt
RUN chmod 0755 cron.sh
RUN touch /var/log/cron.log
RUN crontab cron.sh > /var/log/cron.log
