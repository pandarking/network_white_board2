# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 14:17
# @Author  : Panboshen
# @Email   : 570169891@qq.com
# @File    : whiteboard.py
# @Software: PyCharm
from tkinter import *


class WhiteBoard:
    drawing_tool = 'line'
    line_width = 2
    colors = {'b': 'blue', 'r': 'red', 'g': 'green', 'o': 'orange', 'y': 'yellow', 'pu': 'purple', 'pi': 'pink',
              'd': 'black', 's': 'snow'
              }
    def __init__(self):
        self._init_whiteboard()
        self._init_item_button()
        self._init_color_button()
        self._init_drawing_area()
        self.color = 'd'

    def show_window(self):
        self.myWhiteBoard.mainloop()

    def _init_whiteboard(self):
        self.myWhiteBoard = Tk()
        self.myWhiteBoard.geometry('1200x800')

    def _init_item_button(self):
        Button(self.myWhiteBoard, text='line', height=1, width=5, bg='dark goldenrod', font='Arial',
               command=lambda: self.set_drawing_tool('line')).place(x=70, y=0)
        Button(self.myWhiteBoard, text='rect', height=1, width=5, bg='saddle brown', font='Arial',
               command=lambda: self.set_drawing_tool('rectangle')).place(x=140, y=0)
        Button(self.myWhiteBoard, text='oval', height=1, width=5, bg='NavajoWhite4', font='Arial',
               command=lambda: self.set_drawing_tool('oval')).place(x=210, y=0)
        Button(self.myWhiteBoard, text='text', height=1, width=5, bg='SteelBlue4', font='Arial',
               command=self.get_text_from_user).place(x=280, y=0)
        Button(self.myWhiteBoard, text='pencil', height=1, width=5, bg='DeepSkyBlue2', font='Arial',
               command=lambda: self.set_drawing_tool('pencil')).place(x=350, y=0)
        Button(self.myWhiteBoard, text='circle', height=1, width=5, bg='Turquoise2', font='Arial',
               command=lambda: self.set_drawing_tool('circle')).place(x=420, y=0)
        Button(self.myWhiteBoard, text='square', height=1, width=5, bg='CadetBlue1', font='Arial',
               command=lambda: self.set_drawing_tool('square')).place(x=490, y=0)
        Button(self.myWhiteBoard, text='eraser', height=1, width=5, bg='purple1', font='Arial',
               command=lambda: self.set_drawing_tool('eraser')).place(x=560, y=0)
        Button(self.myWhiteBoard, text='drag', height=1, width=5, bg='green', font='Arial',
               command=lambda: self.set_drawing_tool('drag')).place(x=630, y=0)

    def _init_color_button(self):
        Button(self.myWhiteBoard, height=1, width=5, bg='red',
               command=lambda: self.set_color('red')).place(x=1010, y=50)
        Button(self.myWhiteBoard, height=1, width=5, bg='orange',
               command=lambda: self.set_color('orange')).place(x=1010, y=100)
        Button(self.myWhiteBoard, height=1, width=5, bg='yellow',
               command=lambda: self.set_color('yellow')).place(x=1010, y=150)
        Button(self.myWhiteBoard, height=1, width=5, bg='green',
               command=lambda: self.set_color('green')).place(x=1010, y=200)
        Button(self.myWhiteBoard, height=1, width=5, bg='pink',
               command=lambda: self.set_color('pink')).place(x=1010, y=250)
        Button(self.myWhiteBoard, height=1, width=5, bg='blue',
               command=lambda: self.set_color('blue')).place(x=1010, y=300)
        Button(self.myWhiteBoard, height=1, width=5, bg='purple1',
               command=lambda: self.set_color('purple')).place(x=1010, y=350)
        Button(self.myWhiteBoard, height=1, width=5, bg='black',
               command=lambda: self.set_color('black')).place(x=1010, y=400)
        Button(self.myWhiteBoard, height=1, width=5, bg='snow',
               command=lambda: self.set_color('snow')).place(x=1010, y=450)

    def set_drawing_tool(self, tool):
        self.drawing_tool = tool

    def set_color(self, color):
        color_to_set = [k for k,v in self.colors.items() if v == color]
        if len(color_to_set) == 1:
            self.color = color_to_set[0]
        else:
            print('Unknown color,please reset')

    def get_text_from_user(self):
        self.drawing_tool = 'text'

    def _init_drawing_area(self):
        self.drawing_area = Canvas(self.myWhiteBoard, width=1000, height=740, bg='white')
        self.drawing_area.place(y=40)

    def draw_line(self, msglist):
        startX, startY, endX, endY = int(msglist[1]), int(msglist[2]), int(msglist[3]), int(msglist[4])
        color = msglist[5]
        self.drawing_area.create_line(startX, startY, endX, endY, fill=color, width=self.line_width)

    def draw_from_msg(self, msg):
        msglist = msg.split()
        draw_type = msglist[0]
        if draw_type == 'D':
            self.draw_line(msglist)
        else:
            pass


if __name__ == '__main__':
    wb = WhiteBoard()



















