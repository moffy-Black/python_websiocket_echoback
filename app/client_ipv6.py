import socket
import sys
from datetime import datetime

HOST = 'localhost'
PORT = 8080
s = None
message = sys.argv[1]

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonnam, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
with s:
    s.sendall(message.encode('utf-8'))
    data = s.recv(1024)
print('[{}] Received'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')), repr(data))