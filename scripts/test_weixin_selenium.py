import json

from selenium import webdriver
import time

# 注：没用到PO模式
# 定义pytest的WeChat网页测试类
class TestWechat():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://wx2.qq.com/?&lang=zh_CN')
        time.sleep(10)

        cookie = self.driver.get_cookies()
        with open('cookie.txt', 'w')as f:
            json.dump(cookie, f)

    def test_weixin(self):
        with open('cookie.txt', 'r')as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://wx2.qq.com/?&lang=zh_CN')
        # time.sleep(5)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@placeholder="搜索"]').send_keys('2222')
        time.sleep(4)
        # assert username == 'yezi_i'

    def teardown(self):
        self.driver.quit()
