# flask-pythonpoc

FROM ubuntu:16.04
MAINTAINER Nitesh Singh <niteshkumar.singh@deancare.com>

RUN apt-get update
RUN apt-get install -y python-pip python-dev python-virtualenv gunicorn


# Setup flask application
RUN mkdir -p /deploy/app/pythonpoc
COPY . /deploy/app/pythonpoc/
#COPY src /deploy/src
WORKDIR /deploy/app/pythonpoc/
RUN pip install -r /deploy/app/pythonpoc/requirement.txt

EXPOSE 5000

# Start gunicorn
CMD ["/usr/bin/gunicorn", "--config", "/deploy/app/pythonpoc/config.py", "restcall:app"]
