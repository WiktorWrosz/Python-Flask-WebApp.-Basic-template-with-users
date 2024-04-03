from flask import Flask                 # 1st first thing to do while creating flask app - Import Flask to create a Flask app
from flask_sqlalchemy import SQLAlchemy #  Import SQLAlchemy for database management


db=SQLAlchemy()                         #  Initialize SQLAlchemy for database operations by Create object db.
DB_NAME = "databse.db"

def create_app():                       # create a flask application 'app'
    app = Flask(__name__)               # Use __name__ for the app's name. __name__ is a special variable representing module's name. When a Python file containing __name__ is imported into another program, __name__ takes on the value of the name of the module (or program) it got imported into. If run directly __name__ == "__main__"
    app.config['SECRET_KEY'] = '1234'   # Set a secret key for the app

# Configure the SQLAlchemy database URI to store the database in the same folder as this file __init__.py ( which is website folder).
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' 
    db.init_app(app)                    # Initialize SQLAlchemy for use with Flask

    from .views import views    # imports blueprints view and auth to this file __init__.py
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') # and register blueprints view and auth
    app.register_blueprint(auth, url_prefix='/') # url_prefix='/'  =how to access URL-s stored in blueprints view and auth. '/' - access directly, no needed for example /auth/<name of route> 

    return app                          # return 'app' from function create_app()