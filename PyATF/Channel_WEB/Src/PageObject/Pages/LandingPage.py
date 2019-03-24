__author__ = 'Vikram C'

from selenium.webdriver.common.by import By

from Channel_WEB.Src.PageObject.Locators import Locator


class Landing(object):

    def __init__(self, driver):
        self.driver = driver

# home page locators defining
        self.logo = driver.find_element(By.XPATH, Locator.logo)
        self.sign_in = driver.find_element(By.XPATH, Locator.sign_in)


    def getLogo(self):
        return self.logo

    def getSignIn(self):
        return self.sign_in




