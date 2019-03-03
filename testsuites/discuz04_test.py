from testsuites.base_testcase import BaseTestcase
from pageobjects import discuz01_page,discuz04_page
import time
from framework.logger import Logger
import unittest

logger=Logger(logger="Discuz04_test").get_log()
class Discuz04_test(BaseTestcase):
    def test_discuz04(self):
        discuz04=discuz04_page.Discuz04_page(self.driver)
        discuz01=discuz01_page.Discuz01_page(self.driver)
        discuz01.login("guoqiao","guoqiao")
        time.sleep(3)
        discuz01.morenbankuai()
        time.sleep(2)
        discuz04.toupiao_tie("你最擅长的语言","Java","Python","C++")
        time.sleep(2)
        discuz04.toupiao_process()
        time.sleep(2)
        discuz04.toupiao_info()
        discuz01.tuichu()

    if __name__ == '__main__':
        unittest.main()
