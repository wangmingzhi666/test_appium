# coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import POLL_FREQUENCY


class Base_Action:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def find_element(self, loc):
        return self.driver.find_element(by=loc[0], value=loc[1])

    def click(self, loc):
        self.find_element(loc).click()

    def input(self, loc, text):
        find = self.find_element(loc)
        find.send_keys(text)

    def get_text(self, loc):
        return self.find_element(loc).text


