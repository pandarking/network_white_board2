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
    logs = {}
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.network = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.network.bind((self.host, self.port))
        self.network.listen(20)

        print(f'sever listen at {self.port}')
        threading.Thread(target=self.pinger).start()

    # 心跳线程
    def pinger(self):
        while 1:
            time.sleep(1)
            for client in Server.clients:
                try:
                    msg = 'ß'.encode('ISO-8859-1')
                    # print('ß')
                    client.client_socket.send(msg)
                except ConnectionResetError:
                    print('ConnectionResetError')
                    client.terminate()
                    Server.clients.remove(client)
                except ConnectionAbortedError:
                    client.terminate()
                    Server.clients.remove(client)
                    print('ConnectionAbortedError')

    def start(self):
        while 1:
            client_socket, client_address = self.network.accept()
            print(f'client {client_address} connected')
            client_socket.send('HLO'.encode())
            # time.sleep(0.1)

            msg = ' '
            for client in Server.clients:
                msg = msg + ' ' + client.client_id

            client_socket.send(msg.encode('utf-8'))

            client_thread = threading.Thread(target=self.wait_for_user_nickname, args=[client_socket])
            client_thread.start()

    def wait_for_user_nickname(self, client_socket):
        new_client_id = client_socket.recv(1024).decode('utf-8')
        for msg in Server.logs.values():
            client_socket.sendall(msg.encode('ISO-8859-1'))
        client = Client(client_socket, new_client_id)
        Server.clients.append(client)
        client.start()


class Client:
    msgId = 0
    def __init__(self, client_socket, client_id):
        self.client_socket = client_socket
        self.client_id = client_id
        self._run = True

    def terminate(self):
        self._run = False

    def start(self):
        while self._run:
            msg = ''
            while 1:
                data = self.client_socket.recv(1).decode('ISO-8859-1')
                msg += data
                if data == 'Ø':
                    break
            Server.logs[Client.msgId] = msg
            if msg[0] in ['D', 'R', 'L', 'O']:
                self.broadcast2clients(msg)
            Client.msgId += 1

    def broadcast2clients(self, msg):
        msg = msg.encode('ISO-8859-1')
        for client in Server.clients:
            client.client_socket.sendall(msg)


if __name__ == '__main__':
    server = Server('0.0.0.0', 6000)
    server.start()






