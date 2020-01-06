# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 16:17
# @Author  : Panboshen
# @Email   : 570169891@qq.com
# @File    : Server.py
# @Software: PyCharm
import socket
import time
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.network = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.network.bind((self.host, self.port))
        self.network.listen(20)

        print(f'sever listen at {self.port}')

    def start(self):
        while 1:
            client_socket, client_address = self.network.accept()
            print(f'client {client_address} connected')
            time.sleep(0.1)
            threading.Thread(target=self.wait_for_user_nickname, args=[client_socket])

    def wait_for_user_nickname(self):
        pass












