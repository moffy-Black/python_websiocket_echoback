import selectors
import socket
import sys

host = 'localhost'
port = 8080
server_address = (host, port)

recv_size = 1024

message = sys.argv[1]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(server_address)
    client_socket.send(message.encode('utf-8'))

    data = client_socket.recv(recv_size)

    print(data.decode('utf-8'))
