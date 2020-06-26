from selenium.webdriver.common.by import By
from base.base_action import Base_Action


class Calculate_Page(Base_Action):
    # 计算结果元素
    result = [By.ID, 'com.miui.calculator:id/result']

    # 计算器功能按键元素
    def cal_button(self, key):
        return [By.XPATH, "//*[@content-desc='"+key+"']"]

    # 计算器数字按键元素
    def num_button(self, num):
        return [By.XPATH, "//*[@text="+num+"]"]

    # 点击数字
    def click_num(self, num):
        num = str(num)
        self.click(self.num_button(num))

    # 点击加号
    def click_add(self):
        self.click(self.cal_button('加'))

    # 点击减号
    def click_substract(self):
        self.click(self.cal_button('减'))

    # 点击乘号
    def click_mulit(self):
        self.click(self.cal_button('乘'))

    # 点击除号
    def click_div(self):
        self.click(self.cal_button('除'))

    # 点击等号
    def click_equal(self):
        self.click(self.cal_button('等于'))

    # 点击清除
    def click_clear(self):
        self.click(self.cal_button('清除'))

    # 获取结果
    def get_result(self):
        return self.get_text(self.result)