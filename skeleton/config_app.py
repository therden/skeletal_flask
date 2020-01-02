from flask import Flask


# configure Flask app -- don't change without understanding!
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')


# The following may be changed to other Bootstrap themes on the Bootswatch site
app.config['FLASK_ADMIN_SWATCH'] = 'cyborg'
