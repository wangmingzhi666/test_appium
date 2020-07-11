import os ,sys
import pytest
from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from base.set_tear import set_tear
from page.search_page import SearchPage
from base.base_yml import read_yml_data_with_file


def data_with_key(key):
    return read_yml_data_with_file('search_data')[key]


class TestSearch():
    def setup_class(self):
        self.driver = set_tear().setup('com.android.settings', '.MiuiSettings')
        self.search_page = SearchPage(self.driver)

    @pytest.mark.parametrize('result_data', data_with_key('data'))
    def test_search(self, result_data):
        self.search_page.search_wlan(result_data)

    def teardown_class(self):
        set_tear().teardown(self.driver)


if __name__ == '__main__':
    pytest.main()
