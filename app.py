#!/usr/bin/env/python3

import os

from flask import Flask, render_template

app = Flask(__name__)

# Read posts directory
path = './posts'
posts = []
with os.scandir(path) as it:
    post_index = 0
    for entry in it:
        if entry.is_file():
            with open(entry.path) as post:
                posts.append({'index':post_index,
                              'title':str(post_index),
                              'data':post.read()})


links = [
    {
        'name':'start',
        'href':'/'
    },
    {
        'name':'posts',
        'href':'/posts'
    },
    {
        'name':'google',
        'href':'https://google.com'
    }
]

@app.route("/")
@app.route("/index")
def show_index():
    title = "gsf's blog"
    return render_template('index.html', title=title,
                           posts=posts, top_links=links)

@app.route("/posts")
def show_posts():
    return render_template('posts.html', title='posts',
                           posts=posts, top_links=links)

@app.route("/posts/<int:index>")
def show_post(index):
    return render_template('post.html', title='post',
                           post=posts[index], top_links=links)

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
