from flask import Flask, escape
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
try: 
    from flaskblog.local_settings import Gmusername, Gmpassword
except:
    print('Email and Username Not Set')
    exit()

app = Flask(__name__)
app.config['SECRET_KEY'] = '588bfc6c02c11378a5e620b0bd1dfb43'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = Gmusername
app.config['MAIL_PASSWORD'] = Gmpassword
mail = Mail(app)


from flaskblog import routes