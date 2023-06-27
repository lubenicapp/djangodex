# DJANGODEX

A Django app inspired by the Pokedex. This is a technical assessment for a job interview.

## Setup


Rename sample.env as .env and configure variable if needed

run `docker-compose --env-file .env up --build`

at this point, the database is empty. I will write later the auto setup but for the moment


in the terminal, run:

`docker exec -it pokedex_db psql -U joe -d djangodex`


then paste the content of the file data/seed.sql

sorry for the inconvenience, will improve later


&nbsp;

You should be able to access http://0.0.0.0:8000/pokedex

You should be able to access http://0.0.0.0:8000/pokedex/14


You can also access '/pokemon/'

and send a post request to /pokemon/create

a notebook helper is provided in tools to try some routes

## Explanation for solution
>>>>>>> develop
