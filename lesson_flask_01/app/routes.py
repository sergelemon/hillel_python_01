from flask import render_template, url_for, redirect, flash
from app import app
from app.forms import PostForm

@app.route('/')
def index():
    messages = app.db.get_posts()
    return render_template('index.html', user='Yehor', messages=messages)

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        flash('Posting your shit')
        return redirect(url_for('index'))
    return render_template('post.html', form=form)

@app.route('/topsecret')
def forbidden():
    return redirect(url_for('index'))
