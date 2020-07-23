# coding=utf-8
import os, sys
sys.path.append(os.getcwd())
from base.set_tear import set_tear
from page.minip_page import minip_page
from base.base_yml import write_yml_to_file
import pytest
import time


class TestMiniP():
    def setup_class(self):
        # com.tencent.mm /.ui.LauncherUI
        self.driver = set_tear().setup('com.tencent.mm', '.ui.LauncherUI')
        self.minip_page = minip_page(self.driver)
        self.minip_page.swipe_into_minip()

    def test_wechat(self):
        self.minip_page.KFC_minip_order()
        self.minip_page.xunzhi()
        time.sleep(5)
        con = self.driver.contexts
        print(con)
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')



    def teardown_class(self):
        set_tear().teardown(self.driver)