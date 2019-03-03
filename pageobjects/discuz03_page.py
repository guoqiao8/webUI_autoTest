from framework.base import BaseTest
from selenium.webdriver.common.by import By
import unittest

class Discuz03_page(BaseTest):
    seach_input_loc=(By.ID,'scbar_txt')
    seach_button_loc=(By.NAME,'searchsubmit')
    seach_tie_name_loc=(By.CSS_SELECTOR,'.xs3 a')
    name_haotest_loc=(By.ID,'thread_subject')

    unit=unittest.TestCase()

    def seach_tie(self,seach_tie_name,assert_name):
        self.current_window()
        self.send_Keys(seach_tie_name,*self.seach_input_loc)
        self.click(*self.seach_button_loc)
        self.window_handles(1)
        self.click(*self.seach_tie_name_loc)
        self.window_handles(2)
        text=self.text(self.find_element(*self.name_haotest_loc))
        self.unit.assertEqual(seach_tie_name,assert_name,msg=seach_tie_name)





