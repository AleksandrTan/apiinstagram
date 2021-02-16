#!/usr/bin/env python

import socket
import json
import _thread as thread


class WSServer:

    def __init__(self):
        self.host = 'localhost'
        self.port = 8001
        self.main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.main_socket.bind((self.host, self.port))
        self.main_socket.listen(5)

        self.start = {"mail": "test@mail.com", "password": "1234567", "bot_id": 1,
                      "params": {},
                      "proxy":
                          {"host": "localhost", "port": 8085}
                      }

        self.stop = {"bot_id": 1}

        self.pong = {"pong": "ok"}

        self.cont = {"status": "ok"}

    def start_server(self):
        print('Start server')
        i = 0
        while True:
            connection, address = self.main_socket.accept()
            i += 1
            if address:
                print('Start thread')
                thread.start_new_thread(self.ws_server, (connection,))

    def ws_server(self, connection):
        while True:
            try:
                data = connection.recv(1024)

                if data == b'ping':
                    connection.sendall(bytes(json.dumps(self.pong), encoding="utf-8"))
                    continue

                if data == b"start":
                    connection.sendall(bytes(json.dumps(self.start), encoding="utf-8"))
                    continue

                if data == b"stop":
                    connection.sendall(bytes(json.dumps(self.stop), encoding="utf-8"))
                    continue

                else:
                    connection.sendall(bytes(json.dumps(self.cont), encoding="utf-8"))
                    continue
            except BrokenPipeError as BPE:
                print("Client disconected!!!")

                return False


if __name__ == "__main__":
    server = WSServer()
    server.start_server()
