from testsuites.base_testcase import BaseTestcase
from pageobjects.discuz01_page import Discuz01_page
import time
from framework.logger import Logger
import unittest

logger=Logger(logger="Discuz01_test").get_log()

class Discuz01_test(BaseTestcase):
    '''测试用例1'''
    def test_discuz_test01(self):
        discuz01=Discuz01_page(self.driver)
        discuz01.login("guoqiao","guoqiao")
        time.sleep(3)
        discuz01.morenbankuai()
        time.sleep(3)
        discuz01.fatie("软件测试1","自动化测试11111")

        discuz01.huitie("Good job!!!!!!!!")
        time.sleep(2)

        discuz01.tuichu()
    if __name__=='__main__':
        unittest.main()



