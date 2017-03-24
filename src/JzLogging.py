#!/usr/bin/env python
# coding:GB18030

"""
FuncName: JzLogging.py
Desc: output log to console and file
Date: 2016-06-21 10:30
Home: http://blog.csdn.net/z_johnny
Author: johnny
"""

from logging.handlers import RotatingFileHandler
import logging
import threading
import ConfigParser

class JzLogging(object):
    def __init__(self, config_logging):
        self.logger = logging.getLogger()
        config = ConfigParser.ConfigParser()
        config.read(config_logging)

        mythread=threading.Lock()
        mythread.acquire()
        # lock
        self.log_file_path = config.get('LOGGING', 'log_file_path')
        self.maxBytes = config.get('LOGGING', 'maxBytes')
        self.backupCount = int(config.get('LOGGING', 'backupCount'))
        self.outputConsole_level = int(config.get('LOGGING', 'outputConsole_level'))
        self.outputFile_level = int(config.get('LOGGING', 'outputFile_level'))
        self.outputConsole = int(config.get('LOGGING', 'outputConsole'))
        self.outputFile = int(config.get('LOGGING', 'outputFile'))
        self.formatter = logging.Formatter('%(asctime)s  - %(filename)s : %(levelname)s  %(message)s')

        mythread.release()
        # unlock

    def outputLog(self):
        """
        output log to console and file
        """
        if self.outputConsole == 1 and not self.logger.handlers:
            # if true ,it should output log in console
            # if logger.handlers list is empty,add list,or writing log

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            self.logger.setLevel(self.outputConsole_level)
            self.logger.addHandler(console_handler)

            if self.outputFile == 1:
                self.file_handler = RotatingFileHandler(self.log_file_path, maxBytes=self.maxBytes, backupCount=self.backupCount)
                # defind RotatingFileHandler: log output path，single file max bytes, max backup number.
                self.file_handler.setFormatter(self.formatter)
                self.logger.setLevel(self.outputFile_level)
                self.logger.addHandler(self.file_handler)
            else:
                pass

        return self.logger

if __name__ == '__main__':
    config_logging = 'logConfig.ini'
    mylog = JzLogging(config_logging)
    logger = mylog.outputLog()


