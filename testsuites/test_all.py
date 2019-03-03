import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from testsuites import base_testcase,discuz01_test,discuz02_test,discuz03_test,discuz04_test
import unittest
import HTMLTestRunner


class BaiDuSeach:
    dir = os.path.dirname(os.path.abspath('.'))
    report_path = dir + "/test_report/"

    suit=unittest.TestSuite()
    suit.addTest(unittest.makeSuite(discuz01_test.Discuz01_test))
    suit.addTest(unittest.makeSuite(discuz02_test.Discuz02_test))
    suit.addTest(unittest.makeSuite(discuz03_test.Discuz03_test))
    suit.addTest(unittest.makeSuite(discuz04_test.Discuz04_test))



    if __name__=='__main__':
        html_report = report_path + '\ result.html'
        fp = open(html_report, "wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="测试报告", description="测试详细信息")
        runner.run(suit)
