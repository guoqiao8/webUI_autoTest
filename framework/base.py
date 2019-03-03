from selenium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.expected_conditions as EC
import os
import time
from framework.logger import Logger

logger=Logger(logger="BaseTest").get_log()

class BaseTest(object):

    def __init__(self,driver):
        self.driver=driver

    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page")

    def back(self):
        self.driver.back()
        logger.info("Click back on current page")

    def quit(self):
        self.driver.quit()
        logger.info("Successful quit from browser")

    def get(self,url):
        self.driver.get(url)
        logger.info("Successful get the URL")

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            logger.info("成功找页面元素---%s" ,loc)
            return self.driver.find_element(*loc)
        except:
            logger.error("页面中未找到%s元素",loc)


    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(loc))
            logger.info("成功找页面元素---%s" ,loc)
            return self.driver.find_elements(*loc)
        except:
            logger.error("页面中未找到%s元素",loc)



    def send_Keys(self,text,*loc):
        ele=self.driver.find_element(*loc)
        # ele.clear()
        try:
            ele.send_keys(text)
            logger.info("输入内容：%s"%text)
        except Exception as e:
            logger.error("未能成功输入内容，错误是：%s"%e)
            self.get_windows_img()

    def clear(self, *loc):
        try:
            ele = self.find_element(*loc)
            # ele.clear()
            logger.info("成功clear")
        except Exception as e:
            logger.error("clear失败")
            self.get_windows_img()

    def click(self,*loc):
        try:
            ele = self.driver.find_element(*loc)
            # ele.clear()
            ele.click()
            logger.info("%s按钮点击成功" , loc )
        except Exception as e:
            logger.error("%s按钮点击失败%s" ,loc,e )
            self.get_windows_img()


    def close(self):
        self.driver.close()
        logger.info("成功关闭浏览器")


    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath("."))+"/screenshots/"
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
        except Exception as e:
            self.get_windows_img()


    def frame(self,*loc):
        try:
            self.driver.switch_to.frame(0)
            logger.info("已找到frame")
        except:
            logger.error("未能找到frame")

    def current_window(self):
        try:
            self.driver.switch_to.window(self.driver.current_window_handle)
            logger.info("激活当前窗口成功")
        except:
            logger.error("激活当前窗口失败")

    def window_handles(self,number):
        try:
            self.driver.switch_to.window(self.driver.window_handles[number])
            logger.info("激活页面成功")
        except:
            logger.error("激活页面失败")

    def text(self,element):
        try:
            ele=element.text
            logger.info("获取文本成功")
            return ele
        except:
            logger.error("获取文本失败")


    def move_to_element(self,*loc):
        try:
            ele=self.find_element(*loc)
            ActionChains(self.driver).move_to_element(ele).perform()
            logger.info("鼠标悬停成功")
        except:
            logger.error("鼠标悬停失败")












