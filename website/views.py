from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user        #current_user is used for checking if the user is logged in or not
from .models import Note                    # Import the Note model from the current package
from . import db                            # Import the db object from the current package

views = Blueprint("views",__name__)         # Define name of this blueprint == views, same as file name for simplicity
                                            # define this file is a blueprint of our app which means it has a bunch of Routes (URL-s) inside
                                            # routes define the mapping between URLs and the functions that handle requests to those URLs. 

@views.route('/', methods=['GET', 'POST'])  # define first route as homepage '/'
@login_required                             # Decorator to ensure the user is logged in before accessing the homepage. You can't access homepage unless you are log in
def home():                                 # whenever we go to '/' home(main website) will run this function
    if request.method == 'POST':            # Check if the request method is POST
        note = request.form.get('note')     # Retrieve the note data from the form
        if len(note) < 1:                   # Check if the note is empty
            flash('Note is too short', category='error')            # Display an error message if the note is too short
        else:
            new_note = Note(data=note, user_id=current_user.id)     # Create a new Note object with the note data and the current user's ID
            db.session.add(new_note)                                # Add the new note to the database session
            db.session.commit()                                     # Commit the transaction to save the new note
            flash('Note added!', category='success')                # Display a success message after adding the note

    return render_template("home.html", user=current_user)      # Passes data of the currently logged-in user to the website.
                                                                # Render the home template and pass the current user object