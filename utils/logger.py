import logging
import os

from logging import handlers

from config import *


class Logger(object):
    def __init__(self,
                 fmt='[%(asctime)s][%(levelname)s]: %(message)s'
                 ):
        self.logger = logging.getLogger()
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(logging.INFO)
        sh = logging.StreamHandler()
        sh.setFormatter(format_str)
        self.logger.addHandler(sh)

        if enable_file:
            logfile = os.path.join(log_dir, 'log.log')
            th = handlers.TimedRotatingFileHandler(filename=logfile,
                                                   when='D',
                                                   backupCount=3)
            th.setFormatter(format_str)
            self.logger.addHandler(th)

    def info(self, info):
        self.logger.info(info)

    def debug(self, info):
        self.logger.debug(info)

    def warning(self, info):
        self.logger.warning(info)

    def exception(self, info):
        self.logger.exception(info)


logger = Logger()

if enable_file:
    import yaml
    paramfile = os.path.join(log_dir, 'param.yaml')
    with open(paramfile, 'w') as fp:
        yaml.dump(log_dir, fp)


