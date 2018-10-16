FROM python:3.7

RUN pip install Flask Flask-SQLAlchemy Flask-Login Flask-Bcrypt

RUN mkdir /app
RUN mkdir /app/itpscheduler

# make sure `flask run` is run from the parent directory of the module itself;
# that is, ~/../..
WORKDIR /app/itpscheduler

ENV FLASK_APP itpscheduler
ENV FLASK_ENV development

EXPOSE 5000

# docker build -t itpscheduler .
# docker run -it -v ~/Projects/itpscheduler:/app/itpscheduler -p 5000:5000 itpscheduler /bin/bash