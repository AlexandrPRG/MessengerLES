import sys
import logging
import logging.handlers
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
every_day_log = logging.handlers.TimedRotatingFileHandler(
    'server.log',
    encoding='utf-8',
    interval=1,
    when='midnight'
)
every_day_log.setFormatter(server_formatter)


if __name__ == '__main__':
    logger_serv.critical('SERVER critical level event')
    logger_serv.error('SERVER error  level event')
    logger_serv.debug('SERVER debug  level event')
    logger_serv.info('SERVER info  level event')
