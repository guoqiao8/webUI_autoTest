from framework.base import BaseTest
from selenium.webdriver.common.by import By
import unittest

class Discuz04_page(BaseTest):
    fatie_button_loc=(By.CSS_SELECTOR,'#newspecial > img')
    faqitoupiao_button_loc=(By.CLASS_NAME,'poll')
    toupiao_title_input_loc=(By.ID,'subject')
    toupiao_select01_input_loc=(By.CSS_SELECTOR,'#pollm_c_1 > p:nth-child(1) > input')
    toupiao_select02_input_loc=(By.CSS_SELECTOR,'#pollm_c_1 > p:nth-child(2) > input')
    toupiao_select03_input_loc=(By.CSS_SELECTOR,'#pollm_c_1 > p:nth-child(3) > input')
    toupiao_button_loc=(By.ID,'postsubmit')
    #进行投票
    radio_input_loc=(By.ID,'option_1')
    jinxingtoupiao_tijiao_button_loc=(By.ID,'pollsubmit')

    #投票选项及比例
    xuanxiang_name_loc=(By.CSS_SELECTOR,'.pvt')
    bili_name_loc=(By.CSS_SELECTOR,'#poll > .pcht > table > tbody > tr > td:nth-child(2)')
    #投票主题
    zhuti_name_loc=(By.ID,'thread_subject')
    #谢谢参与
    xiexiecanyu_loc=(By.CSS_SELECTOR,'.pcht > table > tbody > tr:nth-child(7) > td')

    unit=unittest.TestCase()

    def toupiao_tie(self,toupiao_title,toupiao_select01,toupiao_select02,toupiao_select03):
        self.current_window()
        self.move_to_element(*self.fatie_button_loc)
        self.click(*self.faqitoupiao_button_loc)
        self.send_Keys(toupiao_title,*self.toupiao_title_input_loc)
        self.send_Keys(toupiao_select01,*self.toupiao_select01_input_loc)
        self.send_Keys(toupiao_select02,*self.toupiao_select02_input_loc)
        self.send_Keys(toupiao_select03,*self.toupiao_select03_input_loc)
        self.click(*self.toupiao_button_loc)
        self.unit.assertIsNotNone(self.find_element(*self.jinxingtoupiao_tijiao_button_loc))

    def toupiao_process(self):
        self.current_window()
        self.click(*self.radio_input_loc)
        self.click(*self.jinxingtoupiao_tijiao_button_loc)
        self.unit.assertEqual("您已经投过票，谢谢您的参与",self.text(self.find_element(*self.xiexiecanyu_loc)),msg="您已经投过票")

    def toupiao_info(self):
        self.current_window()
        xuanxiang_name=self.find_elements(*self.xuanxiang_name_loc)
        bili_name=self.find_elements(*self.bili_name_loc)
        print("投票主题：", self.text(self.find_element(*self.zhuti_name_loc)))
        for i in range(0,len(xuanxiang_name)):
            print("投票选项：",self.text( xuanxiang_name[i]),"比例为：",self.text(bili_name[i*2+1]))









