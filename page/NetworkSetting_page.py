from selenium.webdriver.common.by import By
from base.base_action import Base_Action


class NetworkSetting(Base_Action):
    mobile_network = [By.XPATH, "//*[@text='双卡与移动网络']"]
    network_switch = [By.XPATH, "//*[@text='启用数据网络']"]

    def click_mobile_network(self):
        self.click(self.mobile_network)

    def click_network_switch(self):
        self.click(self.network_switch)