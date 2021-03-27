from flask import Flask
from flask_mail import Mail

app = Flask(__name__)


if __name__ == '__main__':
    app.config.update(
        #MAIL_SERVER='smtp@gmail.com',
        #MAIL_PORT=587,
        MAIL_USE_SSL=True,
        MAIL_USERNAME = 'howitrate@hotmail.com',
        MAIL_PASSWORD = 'Orange!1'
    )

    mail = Mail(app)