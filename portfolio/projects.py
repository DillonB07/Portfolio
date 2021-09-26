from flask import Blueprint, render_template

projects = Blueprint('projects', __name__)


@projects.route('/')
def index():
    return render_template('projects.html')


@projects.route('/impulse')
def impulse():
    return render_template('impulseProjectPage.html')


@projects.route('/spotter')
def spotter():
    return render_template('spotterProjectPage.html')
