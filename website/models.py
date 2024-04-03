from . import db                                # from this . folder(website) import what was defined as db ( db=SQLAlchemy() in __init__ )
from flask_login import UserMixin               # custom class that will enhance user objects for Flask login functionality

class User(db.Model, UserMixin):                 # create class User that inherit from class Model inside db object and from UserMixin class 
    id = db.Column(db.Integer, primary_key=True) # our ID is primary_key which is unique identifier
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))            # variables like password in our class uses function db.Column with argument db.String(150) (max lengh)
    first_name = db.Column(db.String(150))
                            # above class is called user model for our database