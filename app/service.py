''' 服务模块，具体的业务逻辑实现'''

from app.socket import socketio
import time


class CountDownTask:
    def __init__(self, name):
        self.__running__ = True
        self.__name__ = name

    def terminate(self):
        self._running = False

    def run(self, n):
        while self.__running__ and n > 0:
            socketio.emit('send', self.__name__ + ':T-minus >>' + str(n))
            n -= 1
            time.sleep(5)