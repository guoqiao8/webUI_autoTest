from selenium import webdriver
import unittest
from framework.browser_engine import BrowserEngine

class BaseTestcase(unittest.TestCase):
    def setUp(self):
        self.browser_engine=BrowserEngine()
        self.browser_engine.open_browser()
        self.driver=self.browser_engine.driver


    def tearDown(self):
        self.browser_engine.quit_browser()
        print("测试结束。。。。。。")