from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
from app.socket import socketio

if __name__ == '__main__':
    socketio.run(app)