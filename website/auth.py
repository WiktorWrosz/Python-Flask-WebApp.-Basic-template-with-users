from flask import Blueprint
         # define this file is a blueprint of our app which means it has a bunch of Routes (URL-s) inside
         # routes define the mapping between URLs and the functions that handle requests to those URLs. 

auth = Blueprint("auth",__name__) # Define name of this blueprint == auth, same as file name for simplicity