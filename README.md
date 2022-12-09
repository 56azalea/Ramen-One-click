# MySQL + Flask Boilerplate Project
### by Serin Jeon & Dahye Jin

Ramen One-click is an application that shows a collection of every kind of ramen. People can purchase different kinds of ramen via this application. Then, those who have bought and tried ramen can post a rating for the product. These ratings can be viewed by anyone who uses Ramen One-click. By collating the users’ ratings, the overall popularity and rate for each product will also be calculated and displayed on the application. Also, there are other functionalities that the user can enjoy. One of them is ramen Mukbang shows by Mukbang creators, featuring specific ramen products registered on the application. Others include ramen-related events and recommendation posts.

## User
webapp is the user, who is granted with all privileges on our database.

## Database (`ramen_db.sql/`)
full_db is the name of our database. Password is required to access, which are recorded in `secrets/` folder.
Tables are created inside full_db, which represent each user type (Customer Service, Customer, Administrator), necessary objects (Ramen Company, Ramen Product, Mukbang Creator, Mukbang Show, Post), as well as the relationships between components mentioned earlier. There are 11 tables total.
After each table creation, there is INSERT INTO method, which adds example data into the corresponding table. For any attributes that are foreign keys, they refer to their parent keys.

## Flask app
Within `flask-app/` folder, there are three parts: `src/`, `app.py/`, and `Dockerfile/`.

### src
There are four new folders made inside src folder, which represent each corresponding wireframe.
1. `one_pick/` is a blueprint and a wireframe for Customer Service, where that user can get public posts and make a new post in the DB. 
1. `ramen_on/` is a blueprint and a wireframe for Customer, where the user can get mukbang shows from the DB.
1. '`register_prod/` is a blueprint and a wireframe for Administrator, where the user can get registerd products, get companies of the registered products, and post a new ramen product to the DB.
1. `review/` is a blueprint and a wireframe for Customer, where the user can post a review for a product to the DB.
1. `__init__.py/` is a python file that contains some set up for the application. webapp is the connected user and full_db is the connected database. This file imports the various routes -- four wireframes mentioned above. Blueprints for each wireframe is registered, which have '/ramen_oneclick' as a common url prefix.

### `app.py/`
app.py file creates the app object using the local host and port 4000.

## `docker-compose.yml/`
This yml file configures the webserver container as well as the mySQL container. The webserver container maps the host port to 8001 to container port 4000. The mySQL container maps the host port 3200 to container port 3306. It uses the db and db root passwords from `secrets/` folder.


## How to use ngrok to connect our database with AppSmith
**Important** - you need Docker Desktop installed
 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
2. Build the images with `docker compose build`
3. Start the containers with `docker compose up`. To run in detached mode, run `docker compose up -d`. 
4. Add a new terminal and and type 'ngrok http 8001'.
5. The ngrok window will give a Forwarding link. Copy the link.
5. Go to AppSmith and click Flask API under Datasources.
6. Click edit on the top right corner and paste the copied link from ngrok to the URL.
7. The databse is now connected with AppSmith.

## Video Link
To watch our video, go to this link: 
