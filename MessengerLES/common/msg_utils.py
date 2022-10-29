import socket
import sys
import traceback

sys.path.append("../")

import json
import time
import os

from CONSTANTS import \
    MAX_PACKAGE_LENGTH, ENCODING, \
    ACTION, USER, TIME, ACCOUNT_NAME, PRESENCE, RESPONSE, ERROR, \
    MESSAGE, MESSAGE_TEXT
from logs import server_log_config, client_log_config


def log(func):
    def wrap(*args, **kwargs):
        path = r'.'
        name_script = traceback.format_stack()[0].strip().split()[-1]
        log_name = name_script[:-2] + '.log'
        f'Функция {func.__name__} вызвана из {name_script}'
        f'параметры вызова: {args}, {kwargs}'
    return wrap

@log
def send_message(socket, msg):
    server_log_config.file_loger.info(
        f'функция {__name__}'
    )
    msg = json.dumps(msg)
    msg = msg.encode(ENCODING)
    socket.send(msg)


@log
def get_message(client):
    client_log_config.file_loger.info(
        f'функция {__name__}'
    )
    msg = client.recv(MAX_PACKAGE_LENGTH)
    msg = msg.decode(ENCODING)
    return json.loads(msg)


@log
def create_presence_msg(account_name='Guest'):
    client_log_config.file_loger.info(
        f'функция {__name__}'
    )
    return {
        ACTION: PRESENCE,
        # TIME: time.time(),
        TIME: 1.1,
        USER: {
            ACCOUNT_NAME: account_name
        }
    }

@log
def process_client_message(msg):
    client_log_config.file_loger.info(
        f'функция {__name__}'
    )
    if ACTION in msg and msg[ACTION] == PRESENCE and TIME in msg \
        and USER in msg and msg[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {'400': 'Bad request'}


# print(create_presence_msg(''))