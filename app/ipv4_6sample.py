import socket
import sys

HOST = None
PORT = 8080
server_socket = None


for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
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
if server_socket is None:
    print('could not open socket')
    sys.exit(1)
client_socket, addr = server_socket.accept()
with client_socket:
    print('Connected by', addr)
    while True:
        data = client_socket.recv(1024)
        if not data: break
        client_socket.send(data)
