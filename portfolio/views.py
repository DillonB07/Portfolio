from flask import render_template, Blueprint, redirect, url_for, request
from .utils import Email, is_human

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html')


@views.route('/about')
def about():
    return render_template('about.html')


@views.route('/projects')
def projects():
    return render_template('projects.html')


@views.route('/tutorials')
def tutorials():
    return render_template('tutorials.html')


@views.route('/contact')
def contact():
    return render_template(
        'contact/contact.html',
        user_name=request.headers['X-Replit-User-Name'],
        user_id=request.headers['X-Replit-User-Id']
    )

@views.route('/contact-sent', methods=['GET', 'POST'])
def contact_logic():
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        captcha_response = request.form['g-recaptcha-response']

        if not is_human(captcha_response):
            print('Bot attempt!')
            return redirect(url_for('views.contact'))

        e = Email(name, id, email, subject, message)
        sent = e.sendEmail()

        if sent:
            return render_template('contact/success.html')
        else:
            return render_template('contact/failure.html')
    else:
        return redirect(url_for('views.contact'))
