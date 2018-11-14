from flask_socketio import SocketIO, emit
from app import app

socketio = SocketIO(app)
@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('post')
def onRecive(json):
    print('received json: ' + str(json))
