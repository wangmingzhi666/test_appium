import pytest
import os, sys
sys.path.append(os.getcwd())
from base.set_tear import set_tear
from page.NetworkSetting_page import NetworkSetting


class TestNetwork():
    def setup_class(self):
        self.driver = set_tear().setup('com.android.settings', '.MiuiSettings')
        self.networksetting = NetworkSetting(self.driver)

    def test_network_change(self):
        self.networksetting.click_mobile_network()
        self.networksetting.click_network_switch()
        self.networksetting.click_network_switch()

    def teardown_class(self):
        set_tear().teardown(self.driver)


    # @pytest.mark.skip(condition='我就是要跳过这个用例啦')
    # @pytest.mark.xfail(True, reason='肯定有问题')
    # @pytest.mark.parametrize('result_data', zip(result_list, check))
    # @pytest.mark.parametrize('result_data', result_list)
    # def test_case01(self, result_data, start):
    #     result = add(3, 4)
    #     assert result == result_data  # 断言失败
    #
    # @pytest.mark.run(order=1)
    # def test_case02(self, start):
    #     result = add(1, 4)
    #     assert result == 5


if __name__ == '__main__':
    pytest.main()