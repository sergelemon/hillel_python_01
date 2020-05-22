from flask import request
from flask import render_template

from app import app

@app.route('/users/start', methods=['POST'])
def users_start():
    if request.method == 'POST':
        print(request.values.get('id'))
    return 'Okay'

@app.route('/')
def index():
    # messages = app.db.get_posts()
    return render_template('index.html')