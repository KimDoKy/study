FROM        container-base
MAINTAINER  makingfunk0@gmail.com

COPY        . /srv/app
WORKDIR     /srv/app

COPY        .conf/uwsgi-app.ini     /etc/uwsgi/sites/app.ini
COPY        .conf/nginx.conf        /etc/nginx/nginx.conf
COPY        .conf/nginx-app.conf    /etc/nginx/sites-available/app.conf
RUN         ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/app.conf
