# DJANGODEX

A Django app inspired by the Pokedex. This is a technical assessment for a job interview.

## Setup


Rename sample.env as .env and configure variable if needed

run `docker-compose --env-file .env up --build`

at this point, the database is empty. I will write later the auto setup but for the moment

in the terminal, run:

`docker exec -it pokedex_db`

then

`psql -U joe -d djangodex` (or with whatever .env variable you've set)

then paste the content of the file data/seed.sql

sorry for the inconvenience, will improve later


&nbsp;

You should be able to access http://0.0.0.0:8000/pokedex

You should be able to access http://0.0.0.0:8000/pokedex/14

## Explanation for solution
