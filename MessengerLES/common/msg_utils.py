import sys
sys.path.append("../")

import json
import time

from CONSTANTS import \
    MAX_PACKAGE_LENGTH, ENCODING, \
    ACTION, USER, TIME, ACCOUNT_NAME, PRESENCE, RESPONSE, ERROR, \
    MESSAGE, MESSAGE_TEXT
from logs import server_log_config, client_log_config


def send_message(socket, msg):
    server_log_config.file_loger.info(
        f'функция {__name__}'
    )
    msg = json.dumps(msg)
    msg = msg.encode(ENCODING)
    socket.send(msg)


def get_message(client):
    client_log_config.file_loger.info(
        f'функция {__name__}'
    )
    msg = client.recv(MAX_PACKAGE_LENGTH)
    msg = msg.decode(ENCODING)
    return json.loads(msg)


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


def process_client_message(msg):
    client_log_config.file_loger.info(
        f'функция {__name__}'
    )
    if ACTION in msg and msg[ACTION] == PRESENCE and TIME in msg \
        and USER in msg and msg[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {'400': 'Bad request'}
