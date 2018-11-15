from app import app
from flask import render_template, flash, redirect, request
from app.forms import LoginForm
from app.socket import socketio

from app.service import CountDownTask
from threading import Thread


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'fangkui'}
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', form=form)


@app.route("/json", methods=['POST', 'GET'])
def getData():
    print(request.get_json())
    # socketio.emit('send', '{"data":"server send a message"}')
    # 创建线程进行执行
    countOne = CountDownTask('count_1')
    countTwo = CountDownTask('count_2')
    threadOne = Thread(target=countOne.run, args=(10, ))
    threadTwo = Thread(target=countTwo.run, args=(10, ))
    threadOne.start()
    threadTwo.start()
    # threadOne.join()
    # threadTwo.join()
    print("Thread running")
    return "request.get_json()"