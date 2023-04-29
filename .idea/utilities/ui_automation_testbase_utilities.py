

from Selenium_Tests.utilities import ui_automation_logger_utilities
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest


import time

DRIVER = None
LOGGER = None

class SeleniumUtilities(unittest.TestCase):


    # def get_logger(self):
    #     global LOGGER
    #     LOGGER = ui_automation_logger_utilities.Logger().get_logger()
    #     return LOGGER

    def chrome_driver(self):
        global DRIVER
        url='http://www.google.com'
        options = Options()
        options.add_argument("--start-maximized")

        DRIVER = webdriver.Chrome(r"C:\webdriver\chromedriver.exe",options=options)
        return DRIVER

    def firefox_driver(self):
        global DRIVER
        DRIVER = webdriver.firefox()
        return DRIVER

    def return_driver(self):
        return DRIVER

    def print_message(self):
        print('test is successfull')

    def launch_browser(self,url):
        DRIVER = self.Chrome_driver()
        DRIVER.get(url)


    def wait(self, wait_time=1):
        """
        This method will make the script wait for given seconds default wait time is 1
        :param wait_time: user should provide the time that user want.
        :return:
        """
        time.sleep(wait_time)


def main_chrome():
    D = SeleniumUtilities()
    return D