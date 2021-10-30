from flask import render_template, Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html')


@views.route('/about')
def about():
    return render_template('about.html')


@views.route('/contact')
def contact():
    return render_template('contact.html')


@views.route('/projects')
def projects():
    return render_template('projects.html')


@views.route('/tutorials')
def tutorials():
    return render_template('tutorials.html')
