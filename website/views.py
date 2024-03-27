from flask import Blueprint
         # define this file is a blueprint of our app which means it has a bunch of Routes (URL-s) inside
         # routes define the mapping between URLs and the functions that handle requests to those URLs. 

views = Blueprint("views",__name__) # Define name of this blueprint == views, same as file name for simplicity

@views.route('/')                   # define first route as homepage /
def home():                         # whenever we go to '/' home(main website) will run this function
    return "<h1>Test</h1>"