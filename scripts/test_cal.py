import os, sys
sys.path.append(os.getcwd())
from base.set_tear import set_tear
from page.calculate_page import Calculate_Page
import pytest


class TestCalculate():
    def setup_class(self):
        self.driver = set_tear().setup('com.miui.calculator', '.cal.CalculatorActivity')
        self.calculate_page = Calculate_Page(self.driver)

    def test_add(self):
        self.calculate_page.click_num(9)
        self.calculate_page.click_add()
        self.calculate_page.click_num(1)
        self.calculate_page.click_equal()
        result = self.calculate_page.get_result()
        assert result == '= 10'
        self.calculate_page.click_clear()

    def test_substract(self):
        self.calculate_page.click_num(9)
        self.calculate_page.click_substract()
        self.calculate_page.click_num(1)
        self.calculate_page.click_equal()
        result = self.calculate_page.get_result()
        assert result == '= 8'
        self.calculate_page.click_clear()

    def test_multi(self):
        self.calculate_page.click_num(9)
        self.calculate_page.click_mulit()
        self.calculate_page.click_num(1)
        self.calculate_page.click_equal()
        result = self.calculate_page.get_result()
        assert result == '= 9'
        self.calculate_page.click_clear()

    def test_div(self):
        self.calculate_page.click_num(9)
        self.calculate_page.click_div()
        self.calculate_page.click_num(1)
        self.calculate_page.click_equal()
        result = self.calculate_page.get_result()
        assert result == '= 9'
        self.calculate_page.click_clear()

    def teardown_class(self):
        set_tear().teardown(self.driver)


if __name__ == '__main__':
    pytest.main()