# MySQL + Flask Boilerplate Project
### by Serin Jeon & Dahye Jin

(elevator pitch)

This repo contains a boilerplate setup for spinning up 2 docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API

## User
webapp is the user, who is granted with all privileges on our database.

## Database (`ramen_db.sql/`)
full_db is the name of our database. Password is required to access, which are recorded in `secrets/` folder.
Tables are created inside full_db, which represent each user type (Customer Service, Customer, Administrator), necessary objects (Ramen Company, Ramen Product, Mukbang Creator, Mukbang Show, Post), as well as the relationships between components mentioned earlier. There are 11 tables total.
After each table creation, there is INSERT INTO method, which adds example data into the corresponding table. For any attributes that are foreign keys, they refer to their parent keys.


## How to setup and start the containers
**Important** - you need Docker Desktop installed
 
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the `webapp` user. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

## For setting up a Conda Web-Dev environment:

1. `conda create -n webdev python=3.9`
1. `conda activate webdev`
1. `pip install flask flask-mysql flask-restful cryptography flask-login`
