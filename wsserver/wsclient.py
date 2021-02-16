#! /usr/bin/env python

import socket


def client_fbi():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = "localhost"
        port = 8001

        s.connect((host, port))
        while True:
            data = input("Enter you data - ")
            if data == 'q':
                s.close()
                return None
            s.sendall(data.encode())
            print(str(s.recv(4096), 'utf-8'))


client_fbi()
