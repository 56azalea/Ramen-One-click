# Some set up for the application 

from flask import Flask
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()

def create_app():
    app = Flask(__name__)
    
    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'

    # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'webapp'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_password.txt').readline()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'full_db'  # Change this to your DB name

    # Initialize the database object with the settings above. 
    db.init_app(app)
    
    # Import the various routes
    from src.views import views
    # added for Ramen One-Click
    from src.ramen_on.ramen_on import ramen_on_cust
    from src.register_prod.register_prod import register_prod_admin
    from src.one_pick.one_pick import one_pick_serivce

    # Register the routes that we just imported so they can be properly handled
    app.register_blueprint(views,       url_prefix='/ramen_oneclick')
    # added for Ramen One-Click
    app.register_blueprint(ramen_on_cust, url_prefix='/ramen_oneclick/customer')
    app.register_blueprint(register_prod_admin, url_prefix='/ramen_oneclick/admin')
    app.register_blueprint(one_pick_serivce, url_prefix='/ramen_oneclick/cust_service')

    return app