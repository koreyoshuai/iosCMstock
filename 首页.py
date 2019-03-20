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

# 滑动（iphone 6 375,667）
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
    y1 = int(l[1] * 0.1)  # 起始y坐标
    y2 = int(l[1] * 0.8)  # 终点y坐标
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
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    driver.swipe(x1, y1, x2-x1, 0, t)
# 登录按钮
def login():
    l = getSize()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.45)
    TouchAction(driver).tap(None, x1, y1).perform()

sleep(5)
# 滑动轮播图
swipLeft(1000)
sleep(1)
c=getSize()
x5 =int(c[0] * 0.25)
y5=int(c[1] * 0.15)
TouchAction(driver).press(x=x5,y=y5).wait(ms=800).release().perform()
#driver.find_element_by_accessibility_id("返回按钮").click()
print("轮播图查看成功")
# 滑动自选行情
b=getSize()
x3 = int(b[0] * 0.75)
y3=int(b[1] * (1/3))
x4=int(b[0] * 0.05)
driver.swipe(x3,y3,x4-x3,0,800)
sleep(3)
"""
# 咨询热线
driver.find_element_by_accessibility_id("咨询热线").click()
sleep(5)
#driver.set_value(driver.find_element_by_accessibility_id("请问您想问点什么呢 ~ ~"), '你好')
driver.find_element_by_accessibility_id("发送").click()
try:
    driver.find_element_by_accessibility_id("请输入手机号").clear()
except BaseException as e:
    print("已登录彩猫账号")
else:
    driver.set_value(driver.find_element_by_accessibility_id("请输入手机号"), '15558207835')
    driver.set_value(driver.find_element_by_accessibility_id("请输入您的密码"), '123456a')
    sleep(3)
    driver.find_element_by_accessibility_id("登录").click()
    sleep(3)
driver.find_element_by_accessibility_id("返回按钮").click()

# 新手学堂
driver.find_element_by_accessibility_id("新手学堂").click()
sleep(3)
driver.find_element_by_accessibility_id("第一课：1分钟看懂K线图").click()
sleep(2)
driver.find_element_by_accessibility_id("返回按钮").click()
driver.find_element_by_accessibility_id("返回按钮").click()

# 独家策略
driver.find_element_by_accessibility_id("独家资讯").click()
sleep(3)
try:
    driver.find_element_by_accessibility_id("方向:").click()
except BaseException as e:
    print("未跳转到操作建议页面")
else:
    print("成功跳转到操作建议页面")
    driver.find_element_by_accessibility_id("返回按钮").click()
sleep(2)
driver.find_element_by_accessibility_id("首页").click()

# 财经日历
try:
    driver.find_element_by_accessibility_id("财经日历").click()
except BaseException as e:
    pass
else:
    sleep(2)
    try:
        driver.find_element_by_accessibility_id("筛选").click()
    except BaseException as e:
        print("未跳转到财经日历页面")
        driver.find_element_by_accessibility_id("返回按钮").click()
    else:
        print("成功跳转到财经日历页面")
        driver.find_element_by_accessibility_id("确定").click()
        sleep(2)
        driver.find_element_by_accessibility_id("首页").click()
"""
# 浏览7*24小时快讯
sleep(2)
driver.find_element_by_accessibility_id("24h快讯").click()
sleep(3)
swipeUp(1000)
swipeUp(1000)
sleep(2)
swipeDown(1000)
swipeDown(1000)
swipeDown(1000)
sleep(3)
# 实时解盘
def fenxishi():
    l = getSize()
    x1 = int(l[0] * 0.55)
    y1 = int(l[1] * 0.58)
    TouchAction(driver).tap(None,x1,y1).perform()
fenxishi()
sleep(2)
driver.find_element_by_class_name("XCUIElementTypeCell").click()
sleep(2)
driver.set_value(driver.find_element_by_accessibility_id("向分析师提问吧～"),"1")
sleep(2)
driver.find_element_by_accessibility_id("发送").click()
sleep(3)
try:
    driver.find_element_by_accessibility_id("请输入手机号").clear()
except BaseException as e:
    print("已登录彩猫账号")
else:
    driver.set_value(driver.find_element_by_accessibility_id("请输入手机号"), '15558207835')
    driver.set_value(driver.find_element_by_accessibility_id("请输入您的密码"), '123456a')
    sleep(3)
    login()
    sleep(3)
    driver.find_element_by_class_name("XCUIElementTypeCell").click()
    sleep(2)
    driver.set_value(driver.find_element_by_accessibility_id("向分析师提问吧～"),"1")
    sleep(2)
    driver.find_element_by_accessibility_id("发送").click()
    try:
        driver.find_element_by_accessibility_id("0").click()
    except BaseException as e:
        print("已有其他点赞")
    else:
        print("点赞成功")
    sleep(3)
    driver.find_element_by_class_name("XCUIElementTypeButton").click()
    sleep(3)
    driver.find_element_by_accessibility_id("返回按钮").click()
sleep(2)
print("----首页测试结束-----")

























