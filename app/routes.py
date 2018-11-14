from app import app
from flask import render_template, flash, redirect, request
from app.forms import LoginForm
from app.socket import socketio

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'fangkui'}
    return render_template('index.html', title = 'Home', user= user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect('/')
    return render_template('login.html', form=form)

@app.route("/json", methods=['POST', 'GET'])
def getData():
    print(request.get_json())
    socketio.emit('send', '{"data":"server send a message"}')
    return "request.get_json()"