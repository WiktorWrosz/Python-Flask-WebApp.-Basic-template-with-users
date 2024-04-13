from flask import Flask                 # 1st first thing to do while creating flask app - Import Flask to create a Flask app
from flask_sqlalchemy import SQLAlchemy #  Import SQLAlchemy for database management
from os import path
from flask_login import LoginManager

db=SQLAlchemy()                         #  Initialize SQLAlchemy for database operations by Create object db.
DB_NAME = "databse.db"                  # sets name of database

def create_app():                       # create a flask application 'app'
    app = Flask(__name__)               # Use __name__ for the app's name. __name__ is a special variable representing module's name. When a Python file containing __name__ is imported into another program, __name__ takes on the value of the name of the module (or program) it got imported into. If run directly __name__ == "__main__"
    app.config['SECRET_KEY'] = '1234'   # Set a secret key for the app

    # Configure the SQLAlchemy database URI to store the database in the same folder as this file __init__.py ( which is website folder).
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path.join(app.root_path, DB_NAME)}' 
    db.init_app(app)                    # Initialize SQLAlchemy for use with Flask

    from .views import views    # imports blueprints views and auth to this file __init__.py
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') # and register blueprints view and auth
    app.register_blueprint(auth, url_prefix='/') # url_prefix='/'  =how to access URL-s stored in blueprints view and auth. '/' - access directly, no needed for example /auth/<name of route> 

    from .models import User, Note      # this import is not for making a use of it, but to make sure models.py so database is lunched before app is created
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()              # Create an instance of LoginManager to manage user authentication
    login_manager.init_app(app)                 # Initialize LoginManager to work with the Flask app. This enables login functionality across the application. This line associates the initialized LoginManager with the Flask app, enabling login functionality throughout the application.
    login_manager.login_view = 'auth.login'     # Set the login view. Sends unlogged user to auth.py where login function is. When a user tries to access a protected route without being logged in, Flask will redirect them to this view to prompt them to log in.
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))  # This @decorator loads a user object from the database using the provided user ID stored in the session.
                                        # tells flask how we log in user, what user are we looking for
                                        # If the user is found, it returns the user object; otherwise, it returns None.

    return app                          # return 'app' from function create_app()

def create_database(app):
    if not path.exists('website/' + DB_NAME): # checks if database exist
        db.create_all(app=app)                  # if dosen't exist create db
        print('Created  a NEW DATABSE as there was non detected in your website/ folder !')