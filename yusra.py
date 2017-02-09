from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = "ABCDEF"

@app.route('/')
def index():
    """Landing page for Yusra"""

    return render_template("homepage.html")
    