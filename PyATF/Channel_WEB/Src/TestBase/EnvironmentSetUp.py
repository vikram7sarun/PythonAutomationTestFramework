__author__ = 'Vikram C'

import unittest
import datetime
from selenium import webdriver
import time
from Channel_WEB.Src.PageObject.Pages import LoginPage
from Channel_WEB.Src.PageObject.Pages import LandingPage

class EnvironmentSetup(unittest.TestCase):


#setUP contains the browser setup attributes
    def setUp(self):
        self.driver = webdriver.Chrome("D:/Viki/SELENIUM/SeleniumSoftwares/chromedriver.exe")
        print ("Run Started at :"+str(datetime.datetime.now()))
        print("Chrome Environment Set Up")
        print("------------------------------------------------------------------")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)

        logint = LoginPage(driver)





#tearDown method just to close all the browser instances and then quit
    def tearDown(self):
     if (self.driver!=None):
        print("------------------------------------------------------------------")
        print("Test Environment Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))
        self.driver.close()
        self.driver.quit()