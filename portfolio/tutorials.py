from flask import Blueprint, render_template, redirect, url_for

tutorials = Blueprint('tutorials', __name__)


@tutorials.route('/')
def index():
    return redirect(url_for('views.tutorials'))

# Plain Python tutorials


@tutorials.route('/python/randomNumbers')
def randomNumbers():
    return render_template('tutorials/python/randomNumbers.html')

# Replit tutorials


@tutorials.route('/replit/customDomain')
def customDomain():
    return render_template('tutorials/replit/customDomain.html')


@tutorials.route('/replit/is-a-dev')
def is_a_dev():
    return render_template('tutorials/replit/is-a-dev.html')

# Flask tutorials


@tutorials.route('/flask/googleAuth')
def googleAuth():
    return render_template('tutorials/flask/googleAuth.html')

# Django tutorials


@tutorials.route('/django/reactDjango')
def reactDjango():
    return render_template('tutorials/django/reactDjango.html')
