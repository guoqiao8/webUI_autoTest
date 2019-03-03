import logging
import os
import time

class Logger:
    def __init__(self,logger):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        ch=logging.StreamHandler()
        logger_path=os.path.dirname(os.path.abspath('.'))+'/logs/'
        rq=time.strftime("%Y%m%d%H%M",time.localtime())
        logger_name=logger_path+ rq +".log"
        fh=logging.FileHandler(logger_name)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

        format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(format)
        fh.setFormatter(format)


    def get_log(self):
        return self.logger



