from . import db                                # from this . folder(website) import what was defined as db ( db=SQLAlchemy() in __init__ )
from flask_login import UserMixin               # custom class that will enhance user objects for Flask login functionality
from sqlalchemy.sql import func

class Note(db.Model):                            # By inheriting from db.Model, your classes automatically gain capabilities for defining columns and relationships, making it easier to work with the database consistently.
    id =  db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(9999))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # func.now() get current date automaticaly and will store it in db.DateTime

class User(db.Model, UserMixin):                 # create class User that inherit from class Model inside db object and from UserMixin class 

    id = db.Column(db.Integer, primary_key=True) # our ID is primary_key which is unique identifier
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))            # variables like password in our class uses function db.Column with argument db.String(150) (max lengh)
    first_name = db.Column(db.String(150))
                            # above class is called user model for our database