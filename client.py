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
    Objects = {'line': 'L', 'oval': 'O', 'circle': 'C', 'rectangle': 'R', 'square': 'S', 'erase': 'E', 'drag': 'DR'}
    def __init__(self):
        self.connection = Connection()
        Thread.__init__(self)
        WhiteBoard.__init__(self)
        self._init_mouse_event()
        self.setDaemon(True)
        self.isMouseDown = False
        self.x_pos = None
        self.y_pos = None
        self.x_pos2 = None
        self.y_pos2 = None
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
        self.x_pos2 = event.x
        self.y_pos2 = event.y
        self.draw_object()

    def draw_object(self):
        if self.drawing_tool not in Client.Objects:
            return
        else:
            msg = (Client.Objects[self.drawing_tool], self.x_pos, self.y_pos, self.x_pos2, self.y_pos2, 'red')
            self.connection.send_message(msg)

    def motion(self, event=None):
        if self.isMouseDown and self.drawing_tool == 'pencil':
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























