import smtplib
import os
from email.message import EmailMessage
import requests
import json


class Email:
    def __init__(self, user, id, email, subject, message):
        self.name = user
        self.id = id
        self.email = email
        self.subject = subject
        self.message = message
        self.recipient = os.environ['RECIPIENT']
        self.sender = os.environ["SENDER"]
        password = os.environ['PASSWORD']
        self.server = smtplib.SMTP_SSL('smtp.yandex.com', 465)
        self.server.login(self.sender, password)
        print('Connected')

    def sendEmail(self):
        email = f'Name: {self.name}\nID: {self.id}\nEmail: {self.email}\nSubject: {self.subject}\nMessage: {self.message}'
        msg = EmailMessage()
        msg.set_content(email)
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = self.recipient
        try:
            self.server.send_message(msg)
            print('Email successfully sent')
            # self.confirmation()
            return True
        except Exception as e:
            print(e)
            return False

    def confirmation(self):
        email = f'Hi {self.name}.\n\nThanks for your message.\n\nI\'ll be in touch soon!\n\nThanks,\nDillonB07\n\n\nYour message:\n\nName: {self.name}\nID: {self.id}\nEmail: {self.email}\nSubject: {self.subject}\nMessage: {self.message}'
        msg = EmailMessage()
        msg.set_content(email)
        msg['Subject'] = 'Thank you for contacting me!'
        msg['From'] = self.sender
        msg['To'] = self.email
        try:
            self.server.send_message(msg)
            print('Confirmation email successfully sent')
        except Exception as e:
            print(e)


def is_human(captcha_response):
    """
    Validating recaptcha response from google server
    Returns True captcha test passed for submitted form else returns False.
    """
    secret = os.environ['CAPTCHA_SECRET_KEY']
    payload = {'response': captcha_response, 'secret': secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify",
                             payload)
    response_text = json.loads(response.text)
    return response_text['success']