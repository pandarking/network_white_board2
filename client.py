# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 9:49
# @Author  : Panboshen
# @Email   : 570169891@qq.com
# @File    : client.py
# @Software: PyCharm
import time
from threading import Thread
from connection import Connection
from whiteboard import WhiteBoard


class Client(Thread, WhiteBoard):
    def __init__(self):
        self.connection = Connection()
        Thread.__init__(self)
        WhiteBoard.__init__(self)
        self._init_mouse_event()
        self.setDaemon(True)
        self.isMouseDown = False
        self.x_pos = None
        self.y_pos = None
        self.last_time = None

    def _init_mouse_event(self):
        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress-1>", self.left_button_down)
        self.drawing_area.bind("<ButtonRelease-1>", self.left_button_up)

    def left_button_down(self, event=None):
        self.isMouseDown = True
        self.x_pos = event.x
        self.y_pos = event.y
        self.last_time = time.time()

    def left_button_up(self, event=None):
        self.isMouseDown = False
        print(event.x, event.y)
        self.last_time = None

    def motion(self, event=None):
        if self.isMouseDown:
            now = time.time()
            if now - self.last_time < 0.02:
                # print('too fast')
                return
            self.last_time = now
            msg = ('D', self.x_pos, self.y_pos, event.x, event.y, 'red')
            self.connection.send_message(msg)
            self.x_pos = event.x
            self.y_pos = event.y

    def run(self):
        while 1:
            msg = self.connection.receive_msg()
            self.draw_from_msg(msg)
            if msg == 'xxx':
                pass


if __name__ == '__main__':
    client = Client()
    print('start')
    client.start()
    client.show_window()























