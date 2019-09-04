from flask import request, render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

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
