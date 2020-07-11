from appium import webdriver


class set_tear:
    def setup(self, appPackage, appActivity):
        desire_caps = dict()
        desire_caps['platformName'] = 'Android'
        desire_caps['platformVersion'] = '10'
        desire_caps['deviceName'] = 'ce9bff4'
        desire_caps['appPackage'] = appPackage
        desire_caps['appActivity'] = appActivity
        desire_caps['noReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
        return self.driver

    def teardown(self, driver):
        driver.quit()