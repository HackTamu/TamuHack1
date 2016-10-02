
from flask import Flask
from flask_mail import Mail, Message


app = Flask(__name__)
mail = Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'code.way.2016@gmail.com'
app.config['MAIL_PASSWORD'] = 'Code@Way'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

@app.route('/email')
def email():
    msg = Message('Pending task', sender='code.way.2016@gmail.com', recipients=['kmr.manish@tamu.edu'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"


if __name__ == '__main__':
    app.run()
