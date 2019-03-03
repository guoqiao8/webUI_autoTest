from framework.base import BaseTest
from selenium.webdriver.common.by import By
import unittest

class Discuz02_page(BaseTest):
    login_but = (By.CSS_SELECTOR, '#lsform > div > div > table > tbody > tr:nth-child(2) > td.fastlg_l > button')
    del_input = (By.XPATH, '//*[@id="threadlisttableid"]/tbody[2]/tr/th/a[2]')
    del_button = (By.CSS_SELECTOR, '#modmenu > a:nth-child(1)')
    queding_but = (By.NAME, 'modsubmit')
    guanlizhongxin = (By.CSS_SELECTOR, '#um > p:nth-child(2) > a:nth-child(16)')
    admin_mima_input = (By.CSS_SELECTOR, '#loginform > p:nth-child(6) > input')
    tijiao_but = (By.CSS_SELECTOR, '#loginform > p.loginnofloat > input')
    luntan_link = (By.ID, 'header_forum')

    add_bankuai_link = (By.XPATH, '//*[@class="lastboard"]/a')
    new_bankuai_name = (By.CSS_SELECTOR, '#cpform > table > tbody:nth-child(3) > tr:nth-child(1) > td:nth-child(3) > div > input')
    luntan_tijiao_but = (By.ID, 'submit_editsubmit')

    admin_tuichu = (By.CSS_SELECTOR, '#frameuinfo > p:nth-child(1) > a')
    admin_tuichu2=(By.CSS_SELECTOR,'#um > p:nth-child(2) > a:nth-child(18)')

    new_bankuai_in=(By.CSS_SELECTOR,'#category_1 > table > tbody > tr:nth-child(2) > td:nth-child(2) > h2 > a')

    unit=unittest.TestCase()

    def delete_tie(self):
        self.current_window()
        self.click(*self.del_input)
        self.click(*self.del_button)
        self.click(*self.queding_but)
        assert "默认版块" in  self.driver.title

    def in_luntan(self, admin_mima):
        self.click(*self.guanlizhongxin)
        self.window_handles(1)
        self.send_Keys(admin_mima, *self.admin_mima_input)
        self.click(*self.tijiao_but)
        self.current_window()
        self.click(*self.luntan_link)

    def new_bankuai(self, new_bankuai_name):
        self.window_handles(1)
        self.frame(0)
        self.click(*self.add_bankuai_link)
        self.send_Keys(new_bankuai_name, *self.new_bankuai_name)
        self.click(*self.luntan_tijiao_but)

    def in_new_bankuai(self):
        self.current_window()
        self.click(*self.new_bankuai_in)

    def tuichu_admin(self):
        self.current_window()
        self.click(*self.admin_tuichu)
        self.click(*self.admin_tuichu2)
        self.unit.assertIsNotNone(self.find_element(*self.login_but))

