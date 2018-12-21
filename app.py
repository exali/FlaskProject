from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'matija',
        'title': 'Blog Post 1',
        'content': 'prvi post',
        'date': '2018',
    },
{
        'author': 'matija',
        'title': 'blogpost 2',
        'content': 'drugi post',
        'date': '2018',
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts, title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title='About')


