""""
Функции сервера:
принимает сообщение клиента;
формирует ответ клиенту;
отправляет ответ клиенту;
имеет параметры командной строки:
-p <port> — TCP-порт для работы (по умолчанию использует 7777);
-a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
"""
import sys
sys.path.append("../")
import json
from socket import socket
from socket import SOCK_STREAM, AF_INET
from common.CONSTANTS import DEFAULT_PORT, MAX_CONNECTIONS
from common.msg_utils import get_message, process_client_message
from logs import server_log_config


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
        # print("Неизвестный параметр")
        server_log_config.file_loger.critical(
            f'передан неизвестный параметр {prm}'
        )
        exit(1)
    except IndexError:
        # print(f'Attribute {prm} missing value')
        server_log_config.file_loger.debug(
            f'не хватает значения для переданного {prm}'
        )
        exit(1)
    except ValueError:
        # print('номер порта - число от 1024 до 65535')
        server_log_config.file_loger.critical(
            f'порт менее 1024 ({listen_port})'
        )
        exit(1)


def server():
    listen_addr = pars_prm('-a')
    listen_port = pars_prm('-p')
# сокет сервера
    server_sock = socket(AF_INET, SOCK_STREAM)
    server_sock.bind((listen_addr, listen_port))
    server_sock.listen(MAX_CONNECTIONS)
    while True:
        client, client_addr = server_sock.accept()
        try:
            message_client = get_message(client)
            response = process_client_message(message_client)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('некорректное сообщение от клиента')
            client.close()


if __name__ == '__main__':
    print(sys.path)
    server()
