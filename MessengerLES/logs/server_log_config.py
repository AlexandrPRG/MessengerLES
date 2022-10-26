import sys
import logging
sys.path.append('../')


logger_serv = logging.getLogger('messenger.client')
server_formatter = logging.Formatter("%(asctime)2s %(levelname)s %(module)s %(message)2s")
server_loger = logging.StreamHandler(sys.stderr)
server_loger.setLevel(logging.DEBUG)
server_loger.setFormatter(server_formatter)
file_loger = logging.FileHandler('server.log', encoding='utf-8')
file_loger.setLevel(logging.DEBUG)
file_loger.setFormatter(server_formatter)
logger_serv.addHandler(server_loger)
logger_serv.addHandler(file_loger)
logger_serv.setLevel(logging.DEBUG)


if __name__ == '__main__':
    logger_serv.critical('critical level event')
    logger_serv.error('error  level event')
    logger_serv.debug('debug  level event')
    logger_serv.info('info  level event')
