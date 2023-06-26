# DJANGODEX

A Django app inspired by the Pokedex. This is a technical assessment for a job interview.

## Setup


Rename sample.env as .env and configure variable if needed

run `docker-compose --env-file .env up --build`

at this point, the database is empty. I will write later the auto setup but for the moment

`docker exec -it django_app bash`

then in the container terminal `python manage.py migrate`

&nbsp;

in another terminal:

`docker exec -it pokedex_db`

then

`psql -U joe -d djangodex`

then paste the content of the file data/seed.sql

sorry for the inconvenience, will improve later


&nbsp;

You should be able to access http://0.0.0.0:8000/pokedex

You should be able to access http://0.0.0.0:8000/pokedex/14

## Explanation on solution

I'm more used to Mysql, but i was trapped in a dependency hell on my machine:

```
The following packages have unmet dependencies:
 mariadb-server-10.6 : PreDepends: mariadb-common (>= 1:10.6.12-0ubuntu0.22.04.1) but it is not going to be installed
                       Depends: gawk but it is not installable
                       Depends: libdbi-perl but it is not installable
                       Depends: mariadb-client-10.6 (>= 1:10.6.12-0ubuntu0.22.04.1) but it is not going to be installed
                       Depends: mariadb-server-core-10.6 (>= 1:10.6.12-0ubuntu0.22.04.1) but it is not going to be installed
                       Depends: socat but it is not installable
                       Recommends: libhtml-template-perl but it is not installable
E: Unable to correct problems, you have held broken packages.
```
 
it costs me too much time, then I decided to switch to postgres, but I don't know it well.

This is the reason the auto seed and db setup is not implemented yet
