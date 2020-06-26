class Base_Action:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc):
        return self.driver.find_element(by=loc[0], value=loc[1])

    def click(self, loc):
        self.find_element(loc).click()

    def input(self, loc, text):
        import time
        find = self.find_element(loc)
        time.sleep(2)
        find.send_keys(text)

    def get_text(self, loc):
        return self.find_element(loc).text
