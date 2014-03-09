import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', name='home')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404