from flask import Blueprint, render_template, redirect, url_for

projects = Blueprint('projects', __name__)


@projects.route('/')
def index():
    return redirect(url_for('views.projects'))


@projects.route('/impulse')
def impulse():
    return render_template('projects/impulseProjectPage.html')


@projects.route('/spotter')
def spotter():
    return render_template('projects/spotterProjectPage.html')
