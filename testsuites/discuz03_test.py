from testsuites.base_testcase import BaseTestcase
from pageobjects.discuz01_page import Discuz01_page
from pageobjects.discuz03_page import Discuz03_page
import time
from framework.logger import Logger
import unittest

logger=Logger(logger="Discuz03_test").get_log()
class Discuz03_test(BaseTestcase):
    '''测试用例3'''
    def test_discuz03(self):
        discuz03_test=Discuz03_page(self.driver)
        discuz01_test = Discuz01_page(self.driver)
        discuz01_test.login("guoqiao","guoqiao")
        time.sleep(3)
        discuz03_test.seach_tie("haotest","haotest")
        discuz01_test.tuichu()

    if __name__ == '__main__':
        unittest.main()
