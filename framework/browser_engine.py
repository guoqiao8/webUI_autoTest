import os
from configparser import ConfigParser
from framework.logger import Logger
from selenium import webdriver

logger=Logger(logger="BrowserEngine").get_log()
class BrowserEngine:
    dir=os.path.dirname(os.path.abspath('.'))
    chrome_path=dir+'/tools/chromedriver.exe'
    ie_path=dir+'/tools/IEDriverServer'

    def open_browser(self):
        configparser=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        configparser.read(file_path)

        browser=configparser.get("browserType","name")
        logger.info("成功获取浏览器")
        url=configparser.get("browserServer","name")
        logger.info("成功获取url")

        if browser=="Chrome":
            self.driver=webdriver.Chrome(self.chrome_path)
            logger.info("Starting chrome browser")
        elif browser=="IE":
            self.driver=webdriver.Ie(self.ie_path)
            logger.info("Starting IE browser")

        self.driver.get(url)
        logger.info("open url: %s"%url)
        self.driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds")
        return self.driver

    def quit_browser(self):
        self.driver.quit()




