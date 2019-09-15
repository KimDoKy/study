FROM        container-base
MAINTAINER  makingfunk0@gmail.com

COPY        . /srv/app
WORKDIR     /srv/app

RUN         pip3 install -r requirements.txt
RUN         pip3 install uwsgi
WORKDIR     /srv/app/docker_app
CMD         ["python3", "manage.py", "runserver", "0:8080"]
