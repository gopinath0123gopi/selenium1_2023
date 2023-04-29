

import unittest
import time

from Selenium_Tests.utilities.ui_automation_testbase_utilities import SeleniumUtilities
from Selenium_Tests.utilities import ui_automation_logger_utilities
from Selenium_Tests.utilities.ui_automation_setup_config import PP
from Selenium_Tests.utilities.ui_automation_xpath_interface import PpMainPage


selenium_utilities = SeleniumUtilities()
LOGGER = ui_automation_logger_utilities.Logger().get_logger()
DRIVER = selenium_utilities.chrome_driver()


class TestDesignerLaunch(unittest.TestCase):

    def setUp(self):
        print("start the test  suite")
        super(TestDesignerLaunch, self).setUp()


    def test_pp_homepage(self):
        LOGGER.info("start of test_login_pp ")
        DRIVER.get(PP.pp_mainpage)
        element = DRIVER.find_element_by_xpath(PpMainPage.install_upgrade_client)
        time.sleep(5)

        if element.is_displayed():
            print(" install/upgrade client option available")
        LOGGER.info("end of test_login_pp")


    def test_help_center_webport(self):
        DRIVER.get(PP.pp_mainpage)
        DRIVER.find_element_by_xpath(PpMainPage.help_center).click()
        time.sleep(10)
        DRIVER.switch_to_window(DRIVER.current_window_handle)
        time.sleep(2)
        #DRIVER.find_element_by_xpath(PpMainPage.HelpCenter.administrator).click()
        DRIVER.find_element_by_xpath(PpMainPage.webport).click()
        window_after = DRIVER.window_handles[1]
        DRIVER.switch_to_window(window_after)
        time.sleep(5)





    def switchwidnows(self):
        DRIVER.get(PP.pp_mainpage)
        DRIVER.find_element_by_xpath(PpMainPage.help_center).click()
        time.sleep(5)
        DRIVER.switch_to_window(DRIVER.current_window_handle)
        time.sleep(5)
        window_after = DRIVER.window_handles[1]
        DRIVER.switch_to_window(window_after)
        time.sleep(2)
        DRIVER.find_element_by_xpath(PpMainPage.HelpCenter.administrator).click()



    def tearDown(self):
        pass











        #need to track all windows and then close else only one gets closed
        #DRIVER.close()











