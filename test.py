#!/usr/bin/env python3

from websocket_server import WebsocketServer
import time

def start():
    def message_received(client, server, message):
        print(message)
        time.sleep(2)
        # クライアントへメッセージ送信
        server.send_message(client, 'from server 1st message in message_received')
        time.sleep(2)
        # クライアントへメッセージ送信
        server.send_message(client, 'from server 2st message in message_received')

if __name__ == "__main__":
    start()