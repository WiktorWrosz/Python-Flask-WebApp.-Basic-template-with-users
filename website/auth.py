from flask import Blueprint, render_template
         # define this file is a blueprint of our app which means it has a bunch of Routes (URL-s) inside
         # routes define the mapping between URLs and the functions that handle requests to those URLs. 

auth = Blueprint("auth",__name__) # Define name of this blueprint == auth, same as file name for simplicity

@auth.route('/login')             # path/route for login page
def login():
    return render_template("login.html", text="TESTING", user="Wiktor")
 
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("signup.html")