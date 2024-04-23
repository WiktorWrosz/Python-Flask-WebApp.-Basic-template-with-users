from . import db                                # from this . folder(website) import what was defined as db ( db=SQLAlchemy() in __init__ )
from flask_login import UserMixin               # custom class that will enhance user objects for Flask login functionality
from sqlalchemy.sql import func

# below classes are called note and user models for our database
class Note(db.Model):                            # By inheriting from db.Model, your classes automatically gain capabilities for defining columns and relationships, making it easier to work with the database consistently.
    id =  db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(99999))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # func.now() get current date automaticaly and will store it in db.DateTime
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # for every single note we want to store id of a user who created that note. it's done using db.ForeignKey() function

class User(db.Model, UserMixin):                 # create class User that inherit from class Model inside db object and from UserMixin class 

    id = db.Column(db.Integer, primary_key=True) # our ID is primary_key which is unique identifier
    email = db.Column(db.String(1500), unique=True)
    password = db.Column(db.String(15000))         # variables like password in our class uses function db.Column with argument db.String(150) (max lengh)
    first_name = db.Column(db.String(1500))
    notes = db.relationship('Note')              # 'Note' refers to class Note. Creates a relationship between user and a note he created indicating that a user can have multiple notes associated with them