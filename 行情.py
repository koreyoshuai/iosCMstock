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
# 行情编辑
sleep(3)
driver.find_element_by_accessibility_id("行情").click()
sleep(2)
driver.find_element_by_accessibility_id("编辑").click()
sleep(2)
try:
    driver.find_element_by_accessibility_id("删除“[南]白银10g, AG”").click()
except BaseException as e:
    driver.find_element_by_accessibility_id("back icon").click()
else:
    driver.find_element_by_accessibility_id("删除").click()
    sleep(2)
    driver.find_element_by_accessibility_id("back icon").click()
    sleep(2)
    try:
        driver.find_element_by_accessibility_id("[南]白银10g").click()
        sleep(3)
        driver.find_element_by_accessibility_id("info").click()
    except BaseException as  e:
        print("已成功删除白银品种")
    else:
        print("删除白银品种失败")
        driver.find_element_by_accessibility_id("返回按钮").click()
        driver.find_element_by_accessibility_id("返回按钮").click()
driver.find_element_by_accessibility_id("add").click()
sleep(2)
swipeUp(1000)
sleep(2)
swipeDown(1000)
sleep(2)
swipeDown(1000)
sleep(2)

driver.find_element_by_accessibility_id("添加").click()
sleep(2)
driver.find_element_by_accessibility_id("完成").click()
try:
    driver.find_element_by_accessibility_id("[南]白银10g").click()
except BaseException as  e:
    print("添加白银品种失败")
else:
    print("已成功添加白银品种")
# 分时和K线
swipRight(1000)
sleep(3)
driver.find_element_by_accessibility_id("周K").click()
sleep(3)
driver.find_element_by_accessibility_id("5分钟").click()
sleep(3)
driver.find_element_by_accessibility_id("30分钟").click()
sleep(3)
swipRight(500)
driver.find_element_by_accessibility_id("BOLL").click()
sleep(2)
driver.find_element_by_accessibility_id("KDJ").click()
sleep(2)

# 买入和卖出
try:
    driver.find_element_by_name("闪电买入").click()
except BaseException as e:
    driver.find_element_by_accessibility_id("普通模式").click()
    sleep(2)
    driver.find_element_by_name("闪电买入").click()
else:
    pass
try:
    driver.find_element_by_accessibility_id("请输入手机号").clear()
except BaseException as e:
    try:
        driver.set_value(driver.find_element_by_accessibility_id("请输入交易密码"), '123456a')
    except BaseException as e:
        print("南交所账号已登录")
    else:
        sleep(2)
        driver.find_element_by_accessibility_id("登录").click()
else:
    driver.set_value(driver.find_element_by_accessibility_id("请输入手机号"), '15558207835')
    driver.set_value(driver.find_element_by_accessibility_id("请输入您的密码"), '123456a')
    driver.find_element_by_accessibility_id("登录").click()
    sleep(2)
    driver.set_value(driver.find_element_by_accessibility_id("请输入交易密码"), '123456a')
    driver.find_element_by_accessibility_id("登录").click()
    sleep(2)
sleep(2)
driver.find_element_by_accessibility_id("取消").click()
sleep(2)
driver.find_element_by_accessibility_id("闪电模式").click()
driver.find_element_by_accessibility_id("买入").click()
try:
    driver.find_element_by_accessibility_id("卖出").click()
except BaseException as e:
    print("切换到交易页面失败")
else:
    print("成功切换到交易页面")
sleep(2)
# 设置价格提醒
driver.find_element_by_accessibility_id("行情").click()
sleep(2)
driver.find_element_by_accessibility_id("remind").click()
sleep(2)
driver.find_element_by_class_name("XCUIElementTypeSwitch").click()
sleep(2)
driver.find_element_by_accessibility_id("0.00").clear()
sleep(2)
driver.find_element_by_accessibility_id("保存").click()
sleep(2)
print("白银价格提醒设置成功")
sleep(2)
driver.find_element_by_accessibility_id("返回按钮").click()
print("----行情测试结束-----")



















