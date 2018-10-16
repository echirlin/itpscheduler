from flask import render_template, url_for
from itpscheduler import app

@app.route('/')
def home():
    return "Well howdy!"
