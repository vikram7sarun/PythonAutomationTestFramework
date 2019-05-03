__author__ = 'Vikram C'
from selenium import webdriver
from selenium.webdriver.common.by import By

from Channel_WEB.Src.PageObject.Locators import Locator


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    # Login Page locators defining
        self.username_text_box_id = Locator.username
        self.password_text_box_id = Locator.password
        self.sign_in_button_id = Locator.sign_in


    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_text_box_id).clear()
        self.driver.find_element_by_id(self.username_text_box_id).send_keys(username)


    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_text_box_id).clear()
        self.driver.find_element_by_id(self.password_text_box_id).send_keys(password)

    def tap_button(self):
        self.driver.find_element_by_id(self.sign_in_button_id).click()






