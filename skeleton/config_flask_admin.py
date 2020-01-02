from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink

from skeleton.config_app import app
from skeleton.config_db import db
from skeleton import models


# Configure flask-admin
fa = Admin(app, name="Skeletal Flask)", template_mode='bootstrap3')
fa.add_link(MenuLink(name='App Main Page', category='', url='/'))


# Add a ModelView for each table to be accessible through Flask-Admin
fa.add_view(ModelView(models.User, db.session))
fa.add_view(ModelView(models.Post, db.session))
fa.add_view(ModelView(models.Category, db.session))
