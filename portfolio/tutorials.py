from flask import Blueprint, render_template, redirect, url_for

tutorials = Blueprint('tutorials', __name__)


@tutorials.route('/')
def index():
    return redirect(url_for('views.tutorials'))

# Python tutorials


@tutorials.route('/python/randomNumbers')
def randomNumbers():
    return render_template('tutorials/python/randomNumbers.html')


@tutorials.route('/python/passwordHashing')
def passwordHashing():
    return render_template('tutorials/python/passwordHashing.html')

# Domain tutorials


@tutorials.route('/domain/customDomain')
def customDomain():
    return render_template('tutorials/domains/customDomain.html')


@tutorials.route('/domain/customEmail')
def customEmail():
    return render_template('tutorials/domains/customEmail.html')


@tutorials.route('/domain/is-a-dev')
def is_a_dev():
    return render_template('tutorials/domains/is-a-dev.html')

# Flask tutorials


@tutorials.route('/flask/googleAuth')
def googleAuth():
    return render_template('tutorials/flask/googleAuth.html')

# Django tutorials


@tutorials.route('/django/reactDjango')
def reactDjango():
    return render_template('tutorials/django/reactDjango.html')
