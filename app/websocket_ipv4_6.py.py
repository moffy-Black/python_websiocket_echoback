import socket
import threading
import sys

# from concurrent.futures import ThreadPoolExecutor
from datetime  import datetime

host = None
port = 8080
# workers = 10
recv_size = 1024
server_socket = None

def handle():
    for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = res
        try:
            server_socket = socket.socket(af, socktype, proto)
        except OSError as msg:
            server_socket = None
            continue
        try:
            server_socket.bind(sa)
            server_socket.listen(1)
        except OSError as msg:
            server_socket.close()
            server_socket = None
            continue
        break
    return server_socket


# print('[{}] Server startup, thread-pool = {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), workers))
try:
    while True:
        server_socket = handle()
        if server_socket is None:
            print('could not open socket')
            sys.exit(1)
        client_socket, addr = server_socket.accept()
        with client_socket:
            print('Connected by', addr)
            while True:
                data = client_socket.recv(1024)
                if not data:
                    server_socket = None
                    break
                client_socket.send(data)
except KeyboardInterrupt:
    print('[{}] Server stop'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))