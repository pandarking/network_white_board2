# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 10:00
# @Author  : Panboshen
# @Email   : 570169891@qq.com
# @File    : client.py
# @Software: PyCharm
import socket
from UserDialog import UserDialog
import socket
import time


class Connection:
    def __init__(self):
        UserDialog.getUserIp()
        self.host = UserDialog._Ip
        self.port = UserDialog._Port

        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))
        data = self.socket.recv(3).decode()
        print(data)

        UserDialog.getUserNickname()
        self.nickname = UserDialog._Nickname
        self.socket.sendall((self.nickname.encode('utf-8')))

    def start(self):
        while 1:
            time.sleep(0.1)































