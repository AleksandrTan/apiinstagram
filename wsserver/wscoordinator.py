#!/usr/bin/env python

import socket
import json

start = {"mail": "test@mail.com", "password": "1234567", "bot_id": 1,
         "params": {},
         "proxy":
             {"host": "localhost", "port": 8085}
         }

stop = {"bot_id": 1}

pong = {"pong": "ok"}


def wsserver():
    with socket.socket() as s:
        host = 'localhost'
        port = 8001

        s.bind((host, port))
        print(f'socket binded to {port}')

        s.listen()

        con, addr = s.accept()

        with con:

            while True:
                data = con.recv(1024)
                print(data)

                if data == b'ping':
                    con.sendall(bytes(json.dumps(pong), encoding="utf-8"))
                    continue

                if data == b"start":
                    con.sendall(bytes(json.dumps(start), encoding="utf-8"))
                    continue

                if data == b"stop":
                    con.sendall(bytes(json.dumps(stop), encoding="utf-8"))
                    continue

                con.sendall(data)


wsserver()
