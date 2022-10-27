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
import sys


sys.path.append("../")
import json
from socket import socket
from socket import SOCK_STREAM, AF_INET
from common.msg_utils import create_presence_msg, get_message, send_message
from common.CONSTANTS import MESSAGE
from logs import client_log_config


def main_client():
    server_addr = sys.argv[1]
    server_port = int(sys.argv[2])
    client_sock = socket(AF_INET, SOCK_STREAM)
    client_sock.connect((server_addr, server_port))
    try:
        msg_to_server = create_presence_msg(MESSAGE)
        msg_to_server = get_message(client_sock)
        send_message(server_addr, msg_to_server)
        client_sock.close()
    except (ValueError, json.JSONDecodeError):
        # print('некорректное сообщение от клиента')
        client_log_config.file_loger.critical(
            f'некорректное сообщение {msg_to_server} от клиента'
        )
        client_sock.close()


if __name__ == '__main__':
    main_client()
