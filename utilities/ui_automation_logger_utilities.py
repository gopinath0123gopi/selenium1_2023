import logging
import os
from selenium.webdriver.remote.remote_connection import LOGGER

LOGGER.setLevel(logging.WARNING)
from sys import stdout
class Logger():

    def __init__(self):
        pass

    def get_logger(self):

        logger = logging.getLogger()
        if logger.handlers:
            logger.handlers = []
        logger.setLevel(logging.DEBUG)


        current_path = os.getcwd()
        logs_folder =current_path + os.sep + "logs" + os.sep
        logs_file_name= "logs.log"
        logs_file_path = logs_folder + logs_file_name
        logging.basicConfig(filename=logs_file_path,
                            format='%(asctime)s [%(module)-4s.%(funcName)-3s]: - %(levelname)s - %(message)s',
                            level=logging.DEBUG)


        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s [%(module)-4s.%(funcName)-3s]: - %(levelname)s - %(message)s')
        sh.setFormatter(formatter)
        logger.addHandler(sh)
        return logger


