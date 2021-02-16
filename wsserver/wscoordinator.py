#!/usr/bin/env python

import socket


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
                if not data:
                    con.close()
                    break

                con.sendall(data)
            return False


wsserver()
