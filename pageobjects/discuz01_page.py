from framework import base
from selenium.webdriver.common.by import By
import unittest
import time

class Discuz01_page(base.BaseTest):
    name_input_seach_loc=(By.NAME,'username')
    pwd_input_seach_loc = (By.NAME, 'password')
    login_but=(By.CSS_SELECTOR,'#lsform > div > div > table > tbody > tr:nth-child(2) > td.fastlg_l > button')
    morenbankuai_link = (By.CSS_SELECTOR,'#category_1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > h2 > a')
    new_fatie_but=(By.CSS_SELECTOR,'#newspecial > img')
    fatie_title=(By.NAME,'subject')
    fatie_input=(By.XPATH,'/html/body')
    fatie_frame=(By.ID,'e_iframe')
    fatie_submint=(By.ID,'postsubmit')
    huitie_input=(By.ID,'fastpostmessage')
    huitie_but=(By.ID,'fastpostsubmit')
    tuichu_but=(By.CSS_SELECTOR,'#um > p:nth-child(2) > a:nth-child(12)')

    unit=unittest.TestCase()
    assert_login_loc=(By.CSS_SELECTOR,'.vwmy')
    assert_morenbankuai_value_loc=(By.CSS_SELECTOR,'.xs2 > a')
    assert_fatie_loc=(By.CSS_SELECTOR,'#thread_subject')

    def login(self,name,pwd):
        self.send_Keys(name,*self.name_input_seach_loc)
        self.send_Keys(pwd,*self.pwd_input_seach_loc)
        self.click(*self.login_but)
        result=self.text(self.find_element(*self.assert_login_loc))
        self.unit.assertEqual(result,name,msg=result)

    def morenbankuai(self):
        self.current_window()
        self.click(*self.morenbankuai_link)
        result = self.text(self.find_element(*self.assert_morenbankuai_value_loc))
        self.unit.assertEqual(result, "默认版块", msg=result)

    def fatie(self,fatie_title,fatie_content):
        self.current_window()
        self.click(*self.new_fatie_but)
        self.send_Keys(fatie_title,*self.fatie_title)
        self.frame()
        self.send_Keys(fatie_content,*self.fatie_input)
        self.current_window()
        self.click(*self.fatie_submint)
        result=self.text(self.find_element(*self.assert_fatie_loc))
        self.unit.assertEqual(result,fatie_title,msg=result)

    def huitie(self,huitie_content):
        self.current_window()
        self.send_Keys(huitie_content,*self.huitie_input)
        self.click(*self.huitie_but)



    def tuichu(self):
        self.current_window()
        self.click(*self.tuichu_but)
        self.unit.assertIsNotNone(self.find_element(*self.login_but))

















