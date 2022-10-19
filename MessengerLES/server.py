""""
Функции сервера:
принимает сообщение клиента;
формирует ответ клиенту;
отправляет ответ клиенту;
имеет параметры командной строки:
-p <port> — TCP-порт для работы (по умолчанию использует 7777);
-a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
"""
import json
from _socket import socket
import sys

from _socket import SOCK_STREAM, AF_INET

from MessengerLES.CONSTANTS import DEFAULT_ADDR, DEFAULT_PORT, MAX_CONNETCTIONS, ACTION, PRESENCE, TIME, USER, \
    ACCOUNT_NAME, RESPONSE, ERROR


def send_message(client, msg):
    CLIENT_SOCKET = socket(AF_INET, SOCK_STREAM)
    CLIENT_SOCKET.connect((client, DEFAULT_PORT))
    CLIENT_SOCKET.send(msg.encode("utf-8"))


def get_message(msg):
    msg = json.load(msg)
    return msg.decode('utf-8')


def process_client_message(msg):
    if ACTION in msg and msg[ACTION] == PRESENCE and TIME in msg \
        and USER in msg and msg[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {ERROR: 'Bad request'}


def pars_prm(prm: str):
    try:
        if prm in ['-a', '-p']:
            listen_port = DEFAULT_PORT
            listen_addr = ''
            if prm in sys.argv:
                val = sys.argv[sys.argv.index(prm) + 1]
                if prm == '-p':
                    listen_port = int(val)
                    if not 1024 < listen_port < 65535:
                        raise ValueError
                    return listen_port
                elif prm == '-a':
                    listen_addr = val
                    return listen_addr
        else:
            if not len(sys.argv):

                raise AttributeError
    except AttributeError:
        print("Неизвестный параметр")
        exit(1)
    except IndexError:
        print(f'Attribute {prm} missing value')
        exit(1)
    except ValueError:
        print('номер порта - число от 1024 до 65535')
        exit(1)


def server():
    listen_addr = pars_prm('-a')
    listen_port = pars_prm('-p')
# сокет сервера
    server_sock = socket(AF_INET, SOCK_STREAM)
    server_sock.bind((listen_addr, listen_port))
    server_sock.listen(MAX_CONNETCTIONS)
    while True:
        client, client_addr = server_sock._accept()
        try:
            message_client = get_message(client)
            response = process_client_message(message_client)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('некорректное сообщение от клиента')
            client.close()


if __name__ == '__main__':
    server()