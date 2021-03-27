from flask import Flask
from flask_mail import Mail, Message

app = Flask(name)

app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'howitrate@hotmail.com'
app.config['MAIL_PASSWORD'] = 'Orange!1'
app.config['MAIL_DEFAULT_SENDER'] = 'howitrate@hotmail.com'
app.config['MAIL_DEBUG'] = False


mail = Mail(app)
@app.route('/')

def index():

    msg = Message("Hello, from HowItRate",
                  sender= 'howitrate@hotmail.com',
                  recipients=[])

    msg.add_recipient("averdone3@gmail.com")
    mail.send(msg)
    return 'MESSAGE SENT'

if name == 'main':
    app.run(debug=False)
