#!/usr/bin/env/python3

import os

from flask import Flask, render_template

app = Flask(__name__)

# Read posts directory
path = './posts'
posts = []
with os.scandir(path) as it:
    for entry in it:
        if entry.is_file():
            with open(entry.path) as post:
                data = post.read().split('\n', 2)
                if len(data) != 3:
                    print("[-] Bad formatting in post file %s" % entry.name)
                print(data[0], data[1])
                index = data[0]
                title = data[1]
                data = data[2]
                posts.append({'index':int(index),
                              'title':title,
                              'data':data})

posts = sorted(posts, key=(lambda d : d['index']))

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
    return render_template('index.html',
                           title="gsf's blog",
                           posts=posts[::-1][:4],
                           top_links=links)

@app.route("/posts")
def show_posts():
    return render_template('posts.html',
                           title='posts',
                           posts=posts,
                           top_links=links)

@app.route("/posts/<int:index>")
def show_post(index):
    return render_template('post.html',
                           title='post',
                           post=posts[index],
                           top_links=links)

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
