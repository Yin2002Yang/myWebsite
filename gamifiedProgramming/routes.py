# This folder maintains all the routes or atleast tries to anyway...

from flask import render_template
from gamifiedProgramming import app

@app.route('/')
@app.route('/home')
def home_page():
    return render_template("homepage.html")
