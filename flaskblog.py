from datetime import datetime
from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '588bfc6c02c11378a5e620b0bd1dfb43'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

posts = [
    {
        'author': 'Aditya Phadte',
        'title': 'Blog Post 1',
        'content': 'this blog post has no real content',
        'date_posted': '3 SEP 2019'
    },
    {
        'author': 'fname1 lname1',
        'title': 'Blog Post 2',
        'content': 'this blog post also has no real content',
        'date_posted': '3 SEP 2019'
    },
    {
        'author': 'fname2 lname2',
        'title': 'Blog Post 2',
        'content': 'also this blog post has no real content',
        'date_posted': '3 SEP 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "aditya@flaskblog.com" and form.password.data == 'aditya1234':
            flash('Logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Username or password is Incorrect', 'danger')

    return render_template('login.html', title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)