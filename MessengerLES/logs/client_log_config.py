import sys
import logging
sys.path.append('../')


logger_clnt = logging.getLogger('messenger.client')
client_formatter = logging.Formatter("%(asctime)2s %(levelname)s %(module)s %(message)2s")
client_loger = logging.StreamHandler(sys.stderr)
client_loger.setLevel(logging.DEBUG)
client_loger.setFormatter(client_formatter)
file_loger = logging.FileHandler('client.log', encoding='utf-8')
file_loger.setLevel(logging.DEBUG)
file_loger.setFormatter(client_formatter)
logger_clnt.addHandler(client_loger)
logger_clnt.addHandler(file_loger)
logger_clnt.setLevel(logging.DEBUG)


if __name__ == '__main__':
    logger_clnt.critical('CLIENT critical level event')
    logger_clnt.error('CLIENT error  level event')
    logger_clnt.debug('CLIENT debug  level event')
    logger_clnt.info('CLIENT info  level event')
