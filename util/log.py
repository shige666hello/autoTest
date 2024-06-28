import os
import time
import logging

class LogMessage:
    def __init__(self):
        self.title = '测试日志'
        day = time.strftime("%Y%m%d%H", time.localtime(time.time()))
        pad = os.getcwd()
        file_dir = os.path.join(pad, 'logco')
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        file = os.path.join(file_dir, f"{day}.log")
        
        self.logger = logging.getLogger(self.title)
        self.logger.setLevel(logging.INFO)
        
        self.logfile = logging.FileHandler(file)
        self.logfile.setLevel(logging.INFO)
        
        self.control = logging.StreamHandler()
        self.control.setLevel(logging.INFO)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logfile.setFormatter(formatter)
        self.control.setFormatter(formatter)
        
        self.logger.addHandler(self.logfile)
        self.logger.addHandler(self.control)

    def debug_info(self, message):
        self.logger.debug(message)

    def info_log(self, message):
        self.logger.info(message)

    def warning_log(self, message):
        self.logger.warning(message)

    def error_log(self, message):
        self.logger.error(message)
