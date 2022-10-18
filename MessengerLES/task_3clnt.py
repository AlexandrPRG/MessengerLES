""""
Функции клиента:
сформировать presence-сообщение;
отправить сообщение серверу;
получить ответ сервера;
разобрать сообщение сервера;
параметры командной строки скрипта client.py <addr> [<port>]:
addr — ip-адрес сервера;
port — tcp-порт на сервере, по умолчанию 7777.
"""
import json
import time

from _socket import socket
import sys

from _socket import SOCK_STREAM, AF_INET

from MessengerLES.CONSTANTS import DEFAULT_ADDR, DEFAULT_PORT, MAX_CONNETCTIONS, ACTION, PRESENCE, TIME, USER, \
    ACCOUNT_NAME, RESPONSE, ERROR


def send_message(client, msg):
    CLIENT_SOCKET = socket(AF_INET, SOCK_STREAM)
    CLIENT_SOCKET.connect((client, DEFAULT_PORT))
    CLIENT_SOCKET.send(msg.encode("utf-8"))


def create_presence_msg(account_name='Guest'):
    return {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {ACCOUNT_NAME: account_name},
    }


def get_message(msg):
    msg = json.load(msg)
    return msg.decode('utf-8')


def main_client():
    server_addr = sys.argv[1]
    server_port = int(sys.argv[2])
    client_sock = socket(AF_INET, SOCK_STREAM)
    client_sock.connect((server_addr, server_port))
    try:
        msg_to_server = create_presence_msg()
        response = get_message(msg_to_server)
        send_message(server_addr, response)
        client_sock.close()
    except (ValueError, json.JSONDecodeError):
        print('некорректное сообщение от клиента')
        client_sock.close()


if __name__ == '__main__':
    main_client()