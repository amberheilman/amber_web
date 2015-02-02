import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='index')


@app.context_processor
def inject_skillset():
    return dict(skillset={'background-image: url("static/python.png"); height:280px; width:280px;': 'Creating RESTful APIs with Python 2, 3',
    					  'background-image: url("static/jenkins.png"); height:280px; width:280px; background-color: black;': 'Deployment'})


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
