from my_app2 import app, hello 
#from my_app.hello.models import MESSAGES 
from flask import render_template, request 

@app.route('/')
@app.route('/hello')
def hello_world():
    user = request.args.get('user', 'Mahmud')
    return render_template('index.html', user=user)