# DJANGODEX

A Django app inspired by the Pokedex. This is a technical assessment for a job interview.

## Setup

### Setup environment variables

Rename sample.env as .env and configure variable if you want to use custom configuration


### Run the containers

run `docker-compose --env-file .env up --build` in a terminal

### Seed the database

at this point, the tables are created but the database is empty.

in another terminal, run:

`docker exec -it pokedex_db psql -U joe -d djangodex`

then paste the content of the file data/seed.sql


## Usage

The API provide those routes:

GET -  /pokedex/
GET -  /pokedex/<id>

GET -  /pokemon/
GET -  /pokemon/<id>
POST - /pokemon/<id>/give-xp
POST - /pokemon/create

To try the POST routes, a notebook is provided in tools/demo.ipynb
with which you can experiment a basic usage.


## Exercise completion

### Basic requirements

Not done:
- /pokedex/ filter on types and other attributes


### Bonus
Done:
- docker file
- docker-compose POSTGRES
