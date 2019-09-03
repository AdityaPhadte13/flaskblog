from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)