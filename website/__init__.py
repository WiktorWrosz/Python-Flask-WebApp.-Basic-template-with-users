from flask import Flask                 # 1st first thing to do while creating flask app

def create_app():                       # create a flask application 'app'
    app = Flask(__name__)               # __name__ is a special variable representing module's name. When a Python file containing __name__ is imported into another program, __name__ takes on the value of the name of the module (or program) it got imported into. If run directly __name__ == "__main__"
    app.config['SECRET_KEY'] = '1234'   # initialize 'app' it's secret key

    from .views import views    # imports blueprints view and auth to this file __init__.py
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') # and register blueprints view and auth
    app.register_blueprint(auth, url_prefix='/') # url_prefix='/'  =how to access URL-s stored in blueprints view and auth. '/' - access directly, no needed for example /auth/<name of route> 

    return app                          # return 'app' from function create_app()