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
    clients = []
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
            client_socket.send('HLO'.encode())
            time.sleep(0.1)

            msg = ' '
            for client in Server.clients:
                msg = msg + ' ' + client.client_id

            client_socket.send(msg.encode('utf-8'))

            client_thread = threading.Thread(target=self.wait_for_user_nickname, args=[client_socket])
            client_thread.start()

    def wait_for_user_nickname(self, client_socket):
        new_client_id = client_socket.recv(1024).decode('utf-8')
        client = Client(client_socket, new_client_id)
        Server.clients.append(client)
        client.start()


class Client:
    def __init__(self, client_socket, id):
        self.client_socket = client_socket
        self.client_id = id
        self._run = True

    def start(self):
        while self._run:
            time.sleep(0.1)


if __name__ == '__main__':
    server = Server('0.0.0.0', 6000)
    server.start()






