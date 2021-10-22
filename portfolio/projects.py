import requests
from flask import Blueprint, render_template, redirect, url_for

projects = Blueprint('projects', __name__)


@projects.route('/')
def index():
    return redirect(url_for('views.projects'))


@projects.route('/impulse')
def impulse():
    return render_template('projects/impulse.html')


@projects.route('/spotter')
def spotter():
    return render_template('projects/spotter.html')


@projects.route('/dizzle')
def dizzle():
    url = 'https://qapi-api.ml/'
    total_questions = requests.get(f'{url}/statistics/total').json()
    return render_template('projects/dizzle.html', total_questions=total_questions)


@projects.route('/qapi')
def qapi():
    url = 'https://qapi-api.ml/'
    total_questions = requests.get(f'{url}/statistics/total').json()
    return render_template('projects/qapi.html', total_questions=total_questions)
