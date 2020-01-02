# Create the simple example database described in the Flask-Admin Quickstart
# found at https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

from skeleton.config_db import db
import skeleton.models as models

db = models.db
User = models.User
Post = models.Post
Category = models.Category
db.create_all()

admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')
db.session.add(admin)
db.session.add(guest)

py = Category(name='Python')
Post(title='Hello Python!', body='Python is pretty cool', category=py)
p = Post(title='Snakes', body='Ssssssss')
py.posts.append(p)
db.session.add(py)

db.session.commit()
