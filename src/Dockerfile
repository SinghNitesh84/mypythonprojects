# flask-pythonpoc

FROM ubuntu:16.04
MAINTAINER Nitesh Singh <niteshkumar.singh@deancare.com>

RUN apt-get update
#RUN apt-get install -y python3-dev python3-pip python-virtualenv gunicorn

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev python-virtualenv gunicorn \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# Setup flask application
RUN mkdir -p /deploy/app/pythonpoc
COPY . /deploy/app/pythonpoc/
#COPY src /deploy/src
RUN pip3 install -r /deploy/app/pythonpoc/requirement.txt
WORKDIR /deploy/app/pythonpoc/src/

EXPOSE 5000

# Start gunicorn
CMD ["/usr/bin/gunicorn", "--config", "/deploy/app/pythonpoc/src/config.py", "restcall:app"]
