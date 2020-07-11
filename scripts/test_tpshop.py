import os, sys
sys.path.append(os.getcwd())
from base.set_tear import set_tear
from page.tpshop_page import TPshop_page, fake_data
from base.base_yml import write_yml_to_file
import pytest


class TestTPshop():
    def setup_class(self):
        self.driver = set_tear().setup('com.tpshop.malls', '.SplashActivity')
        self.tpshop_page = TPshop_page(self.driver)
        self.tpshop_page.click_mine()
        self.tpshop_page.click_intologin()

    @pytest.mark.parametrize('username, password', fake_data(10))
    def test_login(self, username, password):
        write_yml_to_file([[username, password]], 'generate')
        self.tpshop_page.click_login(username, password)

    def teardown_class(self):
        set_tear().teardown(self.driver)





