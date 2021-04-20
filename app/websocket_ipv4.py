import socket
import threading

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

host = 'localhost'
port = 8080
bind_address = (host,port)

workers = 10

backlog_size = 10
recv_size = 1024

def handle(client_socket):
    remote_addr = client_socket.getpeername() #相手のIPアドレスとポート

    print('[{}] {} - handle connection, start - {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), threading.current_thread().getName(), remote_addr))

    with client_socket:
        while True:
            data = client_socket.recv(recv_size) #dataを受け取るまで繰り返す

            if not data: #dataがNoneだったら繰り返しを停止
                break

            client_socket.send(b'Reply: ' + data) #dataを送り返す

    print('[{}] {} - handle connection, exit - {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), threading.current_thread.getName(), remote_addr))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket: #socketの作成 公式書式
    with ThreadPoolExecutor(max_workers = workers) as executor:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(bind_address) #(HOST,PORT)のタプル型dataを受け渡す.サーバのホスト名,ポート名を設定
        server_socket.listen(backlog_size)

        print('[{}] Server startup, thread-pool = {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), workers))

        try:
            while True:
                client_socket, addr = server_socket.accept()
                executor.submit(handle, client_socket) #ThreadPoolExecutorのタスクの実行

        except KeyboardInterrupt:
            print('[{}] Server stop'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

# AF_INET: ipv4環境.アドレス (およびプロトコル) ファミリーを示す定数で、 socket() の 最初の引数に指定することができます。 AF_UNIX ファミリーをサポート しないプラットフォームでは、 AF_UNIX は未定義となります。システムによってはこれら以外の定数が定義されているかもしれません。
# SOCK_STREAM: ソケットタイプを示す定数で、 socket() の2番目の引数に指定することができます。システムによってはこれら以外の定数が定義されているかもしれません。 (ほとんどの場合、 SOCK_STREAM と SOCK_DGRAM 以外は必要ありません。)
