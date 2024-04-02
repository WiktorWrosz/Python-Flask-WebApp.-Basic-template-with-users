from flask import Blueprint, render_template, request, flash
         # define this file is a blueprint of our app which means it has a bunch of Routes (URL-s) inside
         # routes define the mapping between URLs and the functions that handle requests to those URLs. 

auth = Blueprint("auth",__name__) # Define name of this blueprint == auth, same as file name for simplicity

@auth.route('/login', methods=['GET', 'POST'])             # path/route for login page. 
#making sure signup and login accept POST requests by adding methods=['GET', 'POST'], default is only GET
def login():
    data = request.form
    print(data)
    return render_template("login.html", text="TESTING", user="Wiktor", boolean=True)

 
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
# Defines a route '/sign-up' under the 'auth' blueprint, which accepts both GET and POST requests.

def sign_up():
# Defines a function named 'sign_up' to handle requests to the '/sign-up' route.
    data = request.form
    # Retrieves form data from the request.
    print(data)
    # Prints the form data to the console.

    if request.method == 'POST':
    # Checks if the request method is POST.
        
        email = request.form.get('email')
        # Retrieves the 'email' field value from the form data.
        firstName = request.form.get('firstName')
        # Retrieves the 'firstName' field value from the form data.
        password1 = request.form.get('password1')
        # Retrieves the 'password1' field value from the form data.
        password2 = request.form.get('password2')
        # Retrieves the 'password2' field value from the form data.

        if len(email) < 4:
        # Checks if the length of the email is less than 4 characters.
            flash('Email must be longer than 3 characters.', category='error')
            # Flashes an error message to be displayed to the user.

        elif len(firstName) < 2:
        # Checks if the length of the first name is less than 2 characters.
            flash('First Name must be longer than 1 character.', category='error')
            # Flashes an error message to be displayed to the user.

        elif password1 != password2:
        # Checks if the two passwords provided do not match.
            flash('Your passwords don\'t match', category='error')
            # Flashes an error message to be displayed to the user.

        elif len(password1) < 7:
        # Checks if the length of password1 is less than 7 characters.
            flash('Password must be at least 7 characters', category='error')
            # Flashes an error message to be displayed to the user.

        else:
        # If none of the above conditions are met, indicating successful form submission.
            flash('Account created successfully', category='success') 
            # Flashes a success message to be displayed to the user.

            # Code to add the user to the database would typically go here.

    return render_template("signup.html")
    # Renders the 'signup.html' template and returns it as the response to the request.
