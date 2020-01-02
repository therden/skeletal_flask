# NOTE: By default, this repo creates a non-persistent database in memory.
#
#       To change to a persistent SQLite file, edit config_db.py, commenting
#       out the line containing 'sqlite:///:memory:' and un-commenting the
#       line containing 'sqlite:///skeletal.db'
#

import os.path

if not os.path.isfile('skeleton/skeletal.db'):
    import make_db

#
# NOTE: Import the app variable which points to the Flask config_app (which is
#       set in the __init__.py file in the 'skeleton' app subdirectory.)
#

from skeleton.config_app import app

# NOTE: Using app.run to invoke the built-in flask server, as we're doing in
#       this run.py file is okay for development and demonstration purposes,
#       but _not_ in production.
#

app.run(host="localhost", port=8080)
