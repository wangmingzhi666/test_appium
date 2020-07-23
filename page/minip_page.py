# coding=utf-8
from base.base_action import Base_Action

class minip_page(Base_Action):
    def swipe_into_minip(self):
        self.click(self.Xpath_loc('text', '微信'))
        self.Long_x_swipe()

    def KFC_minip_order(self):
        self.click(self.Xpath_loc('text', '肯德基+'))
        self.click(self.Xpath_loc('text', '开始点餐'))
        self.click(self.Xpath_loc('text', '海南大学店'))
        self.click(self.Xpath_loc('text', 'Take Away'))

    def xunzhi(self):
        self.click(self.Xpath_loc('text', '吮指原味鸡'))
