from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
# flask_login manages which pages we have access to and which not, and store info about logged user

        
auth = Blueprint("auth",__name__)   # Define name of this blueprint == auth, same as file name for simplicity
                                    # define this file is a blueprint of our app which means it has a bunch of Routes (URL-s) inside
                                    # routes define the mapping between URLs and the functions that handle requests to those URLs. 

@auth.route('/login', methods=['GET', 'POST'])      # path/route for login page. 
                                                    #  making sure signup and login accept POST requests by adding methods=['GET', 'POST'], default is only GET

def login():
    if request.method == 'POST':                    # Checks if the request method is POST. That means we manipulate with db and not only GET visit a site.
        email = request.form.get('email')           # retrieves the value entered by the user in a form field with the name "email" on the web page. 
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()        # query db by email
        if user:                                                # if user (exist)
            if check_password_hash(user.password, password):    # checks if hash of given pasword == db hash password
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)                 # 'Remembers' user. Logs in the user with the provided user object and sets the 'remember' option to True,
                                                                # allowing the user to remain logged in even after closing the browser session.
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Wrong Email or does not exist', category='error')

    return render_template("login.html", user=current_user)
 
@auth.route('/logout')                       # Defines a route '/logout' under the 'auth' blueprint.
@login_required                              # Ensures that only logged-in users can access this route.
def logout():
    logout_user()                            # Logs out the current user.
    return redirect(url_for('auth.login'))   # Redirects the user to the login page.

@auth.route('/sign-up', methods=['GET', 'POST']) # Defines a route '/sign-up' under the 'auth' blueprint, which accepts both GET and POST requests.

def sign_up():                               # Defines a function named 'sign_up' to handle requests to the '/sign-up' route.
    data = request.form                      # Retrieves form data from the request.
    print(data)                              # Prints the form data to the console.
    
    if request.method == 'POST':                         # Checks if the request method is POST. That means we manipulate with db and not only GET visit a site.
        email      = request.form.get('email')           # Retrieves the 'email' field value from the form data.
        first_name = request.form.get('firstName')       # Retrieves the 'firstName' field value from the form data.
        password1  = request.form.get('password1')       # Retrieves the 'password1' field value from the form data.
        password2  = request.form.get('password2')       # Retrieves the 'password2' field value from the form data.
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('This email already exist and is registered.', category="error")
            
        elif len(email) < 4:                 # Checks if the length of the email is less than 4 characters.
            flash('Email must be longer than 3 characters.', category='error')      # Flashes an error message to be displayed to the user.
            
        elif len(first_name) < 2:            # Checks if the length of the first name is less than 2 characters.
            flash('First Name must be longer than 1 character.', category='error')  # Flashes an error message to be displayed to the user
            
        elif password1 != password2:         # Checks if the two passwords provided do not match.
            flash('Your passwords don\'t match', category='error')                  # Flashes an error message to be displayed to the user.
            
        elif len(password1) < 7:             # Checks if the length of password1 is less than 7 characters.
            flash('Password must be at least 7 characters', category='error')       # Flashes an error message to be displayed to the user.
            
        else:                                # If none of the above conditions are met, indicating successful form submission.
        
            # Code to add the user to the database would typically go here.
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
                        
            login_user(user, remember=True)            
            flash('Account created successfully', category='success')   # Flashes a success message to be displayed to the user.
            return redirect(url_for('views.home'))
            
    return render_template("signup.html", user=current_user)            # Passes data of the currently logged-in user to the website.
    # Renders the 'signup.html' template and returns it as the response to the request.
