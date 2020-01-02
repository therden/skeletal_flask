from flask_sqlalchemy import SQLAlchemy

from skeleton.config_app import app


# When initialized, this repo uses a non-persistent, in-memory SQLite db.
# To use a persistent db, switch which of the next 2 lines are commented out
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skeletal.db'
#
# NOTE: If you switch from an in-memory to a persistent db file and later want
#       to change back, you'll need to delete or rename the skeleton/skeletal.db
#       file before re-starting the server

# Other settings
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the db object
db = SQLAlchemy(app)
