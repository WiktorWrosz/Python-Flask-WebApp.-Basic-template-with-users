from website import create_app  # imports function from __init__.py in website

app = create_app()

if __name__ == '__main__':  # this line make sure Web Server RUN ONLY if this file(main.py) is executed directly, instead running everytime it's imported. 
    app.run(debug=True)     # runs Web Server/flask application
                            # debug=True means everytime we make change to any of our Python code it's gonna automaticaly re-run the web server 