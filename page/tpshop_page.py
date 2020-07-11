from selenium.webdriver.common.by import By
from base.base_action import Base_Action


# 模拟测试数据
def fake_data(num):
    from faker import Faker
    f = Faker(locale='zh_CN')
    data = [[f.phone_number(), f.password(special_chars=False)] for i in range(num)]
    return data


def Xpath_loc(by, info):
    res = [By.XPATH, "//*[@"+by+"='"+info+"']"]
    return res


class TPshop_page(Base_Action):
    mine = Xpath_loc('text', '我的')
    login = Xpath_loc('resource-id', 'com.tpshop.malls:id/head_img')
    username = Xpath_loc('resource-id', 'com.tpshop.malls:id/mobile_et')
    password = Xpath_loc('resource-id', 'com.tpshop.malls:id/pwd_et')
    xieyi = Xpath_loc('resource-id', 'com.tpshop.malls:id/agree_btn')
    commit = Xpath_loc('text', '登录')


    def click_mine(self):
        self.click(self.mine)

    def click_intologin(self):
        self.click(self.login)

    def click_login(self, username_text, password_text):
        self.input(self.username, username_text)
        self.input(self.password, password_text)
        self.click(self.xieyi)
        self.click(self.commit)





