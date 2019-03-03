from testsuites.base_testcase import BaseTestcase
from pageobjects.discuz01_page import Discuz01_page
from pageobjects.discuz02_page import Discuz02_page
import time
from framework.logger import Logger
import unittest

logger=Logger(logger="Discuz02_test").get_log()
class Discuz02_test(BaseTestcase):
    '''测试用例2'''
    def test_discuz02_test(self):
        discuz02=Discuz02_page(self.driver)
        discuz01=Discuz01_page(self.driver)
        discuz01.login("admin","admin")
        time.sleep(5)
        discuz01.morenbankuai()
        time.sleep(2)
        discuz02.delete_tie()
        time.sleep(3)
        discuz02.in_luntan("admin")
        time.sleep(3)
        discuz02.new_bankuai("runajianceshi")
        discuz02.tuichu_admin()
        time.sleep(2)

        discuz01.login("guoqiao", "guoqiao")
        time.sleep(3)
        discuz02.in_new_bankuai()
        time.sleep(3)
        discuz01.fatie("软件测试1", "自动化测试11111")

        discuz01.huitie("Good job!!!!!!!!")
        time.sleep(2)
        discuz01.tuichu()

    if __name__ == '__main__':
        unittest.main()





