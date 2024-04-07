from flask import Blueprint, render_template
from flask_login import login_required, current_user        #current_user is used for checking if the user is logged in or not

views = Blueprint("views",__name__)         # Define name of this blueprint == views, same as file name for simplicity
                                            # define this file is a blueprint of our app which means it has a bunch of Routes (URL-s) inside
                                            # routes define the mapping between URLs and the functions that handle requests to those URLs. 

@views.route('/')                           # define first route as homepage '/'
@login_required                             # you can't access homepage unless you are log in
def home():                                 # whenever we go to '/' home(main website) will run this function
    return render_template("home.html", user=current_user)      # Passes data of the currently logged-in user to the website.