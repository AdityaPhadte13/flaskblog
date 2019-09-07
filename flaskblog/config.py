try: 
    from flaskblog.local_settings import Gmusername, Gmpassword
except:
    print('Email and Username Not Set')
    exit()

class Config:
    SECRET_KEY = '588bfc6c02c11378a5e620b0bd1dfb43'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = Gmusername
    MAIL_PASSWORD = Gmpassword


