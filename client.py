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

        self.soc_ket = socket.socket()
        self.soc_ket.connect((self.host, self.port))
        data = self.soc_ket.recv(3).decode()
        print(data)

        usernames = self.soc_ket.recv(1024).decode('utf-8')
        userlist = usernames.split()

        while 1:
            UserDialog.getUserNickname()
            self.nickname = UserDialog._Nickname
            if self.nickname in userlist:
                UserDialog.show_error_box('用户名已存在')
            else:
                break
        self.soc_ket.sendall((self.nickname.encode('utf-8')))

    def start(self):
        while 1:
            time.sleep(0.1)

    def recive_msg(self):
        while 1:
            time.sleep(0.1)
            data = self.soc_ket.recv(1).decode('ISO-8859-1')
            if data == 'ß':
                print('ß')
                continue
            else:
                pass


if __name__ == '__main__':
    con = Connection()
    print('start')




























