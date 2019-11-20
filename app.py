#!/usr/bin/env/python3

from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'data':'this is a post cool massa tesão'
    },
    {
        'data':'this is another post haha'
    }
]

links = [
    {
        'name':'google',
        'href':'https://google.com'
    },
    {
        'name':'posts',
        'href':'./posts'
    }
]

@app.route("/")
@app.route("/index")
def index():
    title = "gsf's blog"
    return render_template('index.html', title=title,
                           posts=posts, topLinks=links)

@app.route("/posts")
def posts():
    return render_template('posts.html', title='posts',
                           posts=posts, topLinks=links)

if __name__ == "__main__":
    app.run()
