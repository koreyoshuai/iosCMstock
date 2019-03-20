#coding=utf-8

import os
from selenium import webdriver
from appium import webdriver
from time import sleep

import sys
from appium.webdriver.common.touch_action import TouchAction


PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__), p))


PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__), p))
desired_caps = {}
"""
desired_caps['platformName'] = 'ios'
desired_caps['platformVersion'] ='10.3'
desired_caps['deviceName'] = 'iphone 6'
desired_caps['udid'] = '708e15b720b12ed25af25acc33f77672ffba63f6'
desired_caps['bundleId'] = 'com.xuanXin.PreciousMetals'
"""
desired_caps['platformName'] = 'ios'
desired_caps['platformVersion'] ='11.0.3'
desired_caps['deviceName'] = 'iphone 7'
desired_caps['udid'] = '91474779a1b70dd3d842d522c970436ce69e0de6'
desired_caps['bundleId'] = 'com.xuanXin.PreciousMetals'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 获得机器屏幕大小x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
# 屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.8)  # 起始y坐标
    y2 = int(l[1] * 0.1)  # 终点y坐标
    driver.swipe(x1, y1, 0, y2-y1, t)

# 屏幕向下滑动
def swipeDown(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.25)  # 起始y坐标
    y2 = int(l[1] * 0.75)  # 终点y坐标
    driver.swipe(x1, y1, 0, y2-y1, t)

# 屏幕向左滑动
def swipLeft(t):
    l = getSize()
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.05)
    driver.swipe(x1, y1,x2-x1, 0, t)

# 屏幕向右滑动
def swipRight(t):
    l = getSize()
    x1 = int(l[0] * 0.)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    driver.swipe(x1, y1, x2-x1, 0, t)

sleep(3)
driver.find_element_by_accessibility_id("行情").click()
sleep(3)
driver.find_element_by_accessibility_id("所有品种").click()
sleep(3)


driver.find_element_by_accessibility_id("[南]白银10g").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]铋").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]氧化铈").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]铜").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)
driver.find_element_by_accessibility_id("两日").click()
sleep(4)
driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]氧化镝").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()

sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]氧化铒").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]氧化铕").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)



driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]氧化钆").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]氧化钬").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)


driver.find_element_by_accessibility_id("[南]铟").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]氧化镧").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]氧化镥").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]氧化钕").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]钯").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]氧化镨").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]氧化镨钕").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]铂").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]铑").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

swipeUp(500)
driver.find_element_by_accessibility_id("[南]锑").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]氧化钐").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]锡").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]碲").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]氧化铥").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]钨条").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]氧化钇").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("[南]氧化镱").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)

driver.find_element_by_accessibility_id("南交指数").click()
sleep(4)
driver.find_element_by_accessibility_id("分时").click()
sleep(4)

driver.find_element_by_accessibility_id("两日").click()
sleep(4)

  
sleep(4)

driver.find_element_by_accessibility_id("周K").click()
sleep(4)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("30分钟").click()
sleep(4)

driver.find_element_by_accessibility_id("back icon").click()
sleep(2)









