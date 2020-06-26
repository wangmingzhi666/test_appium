import os ,sys
from selenium.webdriver.common.by import By
sys.path.append(os.getcwd())
from base.base_action import Base_Action


class SearchPage(Base_Action):
    search_place = [By.XPATH, "//android.widget.TextView[@content-desc='搜索']"]
    first_result = [By.XPATH, "//*[@class='android.widget.LinearLayout'][0]"]

    def search_wlan(self, text):
        self.click(self.search_place)
        self.input(self.search_place, text)
        self.click(self.first_result)

