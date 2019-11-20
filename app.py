#!/usr/bin/env/python3

from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'index':'0',
        'title':'firs post!',
        'data':'this is a post cool massa tesão'
    },
    {
        'index':'1',
        'title':'second post',
        'data':'this is another post haha'
    }
]

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
    return "this is post number %s" % index

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
