# **Skeletal Flask**

![Alt text](skeleton/static/dancing_skeletons.png "Two skeletons dancing together")

## A beginner-level web app providing database access through a browser


### What

The app in this repo employs [*SQLAlchemy*](https://www.sqlalchemy.org/), [*Flask*](https://flask.palletsprojects.com/), [*Flask-Admin*](https://github.com/flask-admin/flask-admin), and [*Flask-SQLAlchemy*](https://flask-sqlalchemy.palletsprojects.com/) to let users perform basic CRUD actions (create, read, update, delete) on database records.


### Why

This repo offered as a working example a beginner can study to learn how to move beyond the "all-in-one-file" code that is often encountered in Quickstart examples.

As a GitHub template, it can also be used as a 'skeleton' to serve as the basis for creating new database-backed Flask apps.

### Features

This repo...

1. Illustrates an approach to organizing the parts of a Flask app into directories and files in a way that

    - Keeps separate parts of the application in separate files

    - Avoids the 'circular imports' problem that trips up many beginners when they first attempt the above, by using ```__init.py__``` to tie it all together.

    - Shows how to provide default app configuration values -- and provide a means to over-ride them

2. Makes sure that directories, files, and variables have unique names, in order to reduce ambiguities that might impede a beginner's understanding.

3. Many of the files containing code include comments offering explanation and guidance.

4. Includes an example of using Templates to modify the *Flask-Admin Home* page.



### Installation

The following instructions assume that you have both Python (version 3.5 or higher) and git installed.

    git clone https://github.com/therden/skeletal_flask.git
    cd skeletal_flask
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    deactivate


### Trying it out

With your virtual environment activated, from within the ```skeletal_flask``` directory in a terminal window, type

    source .venv/bin/activate
    python run.py

Then open a web browser and in the address bar enter ```http://localhost:8080```

When you are finished using the app, you can either close the terminal window or use [Ctrl-C] to stop the web server and leave the terminal window open.


### Credits

* Much gratitude and respect to the creators and maintainers of Python and the library modules used in this repository.

* The app is initialized with the toy database example described in the [Flask-Admin Quickstart](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/).

* I found the PNG file with the dancing skeletons at https://jetvein.tumblr.com/post/156176095255/.  I'd appreciate hearing from anyone who can tell me how to contact this Tumblr user -- I'd very much like to get their permission to use this image.
Much gratitude and respect to the creators and maintainers of Python and the library modules used in this repository.
