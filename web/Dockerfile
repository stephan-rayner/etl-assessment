FROM python:3.6
MAINTAINER Stephan Rayner <stephan.rayner@gmail.com>

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "--log-file", "-", "--access-logfile", "-", "--workers", "10", "--keep-alive", "1"]