# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 10:03
# @Author  : Panboshen
# @Email   : 570169891@qq.com
# @File    : UserDialog.py
# @Software: PyCharm

from tkinter import *

class UserDialog:
    _Ip = ''
    _Port = 0
    _Nickname = ''

    @classmethod
    def getUserIp(cls):
        def getUserIpAndPort():
            cls._Ip = e1.get()
            cls._Port = int(e2.get())
            ClientWindow.destroy()

        ClientWindow = Tk()
        ClientWindow.title('White Board Client')
        Label(ClientWindow, text='请输入IP').grid(row=0)
        Label(ClientWindow, text='IP').grid(row=1)
        Label(ClientWindow, text='PORT').grid(row=2)
        e1 = Entry(ClientWindow).grid(row=1, column=1)
        e2 = Entry(ClientWindow).grid(row=2, column=1)

        Button(ClientWindow, text='ok', command=getUserIpAndPort).grid(row=3, column=1)

        ClientWindow.mainloop()

    @classmethod
    def getUserNickname(cls):
        def getUserNicknameinner():
            cls._Nickname = e1.get()
            ClientWindow.destroy()

        ClientWindow = Tk()
        ClientWindow.title('White Board Client')
        Label(ClientWindow, text='请输入昵称').grid(row=0)
        Label(ClientWindow, text='昵称').grid(row=1)
        e1 = Entry(ClientWindow).grid(row=1, column=1)

        Button(ClientWindow, text='ok', command=getUserNicknameinner).grid(row=2, column=1)

        ClientWindow.mainloop()












