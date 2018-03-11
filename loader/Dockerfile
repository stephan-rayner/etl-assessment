FROM python:3.6
MAINTAINER Stephan Rayner <stephan.rayner@gmail.com>

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

CMD python load_script.py