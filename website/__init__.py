from flask import Flask #first thing to do while creating flask app

def create_app():                       # create a flask application 'app'
    app = Flask(__name__)               # create a flask application 'app'
    app.config['SECRET_KEY'] = '1234'   # initialize 'app' it's secret key

    return app                          # return 'app' from function create_app()