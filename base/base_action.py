# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import POLL_FREQUENCY


class Base_Action:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def Xpath_loc(self, by, info):
        res = [By.XPATH, "//*[@" + by + "='" + info + "']"]
        return res

    def find_element(self, loc):
        return self.driver.find_element(by=loc[0], value=loc[1])

    def click(self, loc):
        self.find_element(loc).click()

    def input(self, loc, text):
        find = self.find_element(loc)
        find.send_keys(text)

    def get_text(self, loc):
        return self.find_element(loc).text

    def swipe(self, start_xy, end_xy, duration=None):
        start_x, start_y = start_xy[0], start_xy[1]
        end_x, end_y = end_xy[0], end_xy[1]
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def Long_x_swipe(self):
        start_xy = [430, 420]
        end_xy = [430, 1600]
        start_x, start_y = start_xy[0], start_xy[1]
        end_x, end_y = end_xy[0], end_xy[1]
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration=0)



