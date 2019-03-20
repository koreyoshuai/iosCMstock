#coding=utf-8

import os
from selenium import webdriver
from appium import webdriver
from time import sleep

import sys
from appium.webdriver.common.touch_action import TouchAction


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
    x1 = int(l[0] * 0.05)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    driver.swipe(x1, y1, x2-x1, 0, t)
# 登录按钮
def login():
    l = getSize()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.45)
    TouchAction(driver).tap(None, x1, y1).perform()

# 资讯模块
sleep(3)
print("-----实时快讯-----")
driver.find_element_by_accessibility_id("资讯").click()
sleep(2)
swipeUp(1000)
swipeUp(1000)
sleep(2)
print("-----财经日历-----")
driver.find_element_by_accessibility_id("财经日历").click()
sleep(2)
try:
    driver.find_element_by_accessibility_id("日历_白天").click()
except BaseException as e:
    driver.find_element_by_accessibility_id("日历_黑夜").click()
else:
    pass
sleep(2)
driver.find_element_by_accessibility_id("箭头 向右").click()
try:
    driver.find_element_by_accessibility_id("日历_白天").click()
except BaseException as e:
    driver.find_element_by_accessibility_id("日历_黑夜").click()
else:
    pass
sleep(2)
driver.find_element_by_accessibility_id("筛选").click()
sleep(2)
driver.find_element_by_accessibility_id("欧元区").click()
driver.find_element_by_accessibility_id("韩国").click()
driver.find_element_by_accessibility_id("1星-3星").click()
driver.find_element_by_accessibility_id("事件").click()
driver.find_element_by_accessibility_id("重置").click()
sleep(2)
driver.find_element_by_accessibility_id("美国").click()
driver.find_element_by_accessibility_id("中国").click()
driver.find_element_by_accessibility_id("4星-5星").click()
driver.find_element_by_accessibility_id("确定").click()
sleep(2)
print("-----实战分析-----")
driver.find_element_by_accessibility_id("实战分析").click()
sleep(3)
swipeUp(1000)
sleep(2)

sleep(2)
# 我的模块
print("-----我的模块-----")
driver.find_element_by_accessibility_id("我的").click()
try:
    driver.find_element_by_accessibility_id("请登录").click()
except BaseException as e:
    sleep(2)
    print("已登录彩猫账号")
else:
    driver.find_element_by_accessibility_id("请输入手机号").clear()
    driver.set_value(driver.find_element_by_accessibility_id("请输入手机号"), '15558207835')
    driver.set_value(driver.find_element_by_accessibility_id("请输入您的密码"), '123456a')
    sleep(3)
    login()
    sleep(3)
driver.find_element_by_accessibility_id("大佬_").click()
sleep(2)
driver.find_element_by_accessibility_id("头像").click()
driver.find_element_by_accessibility_id("相册").click()
try:
    driver.find_element_by_accessibility_id("确定").click()
except BaseException as e:
    pass
else:
    print("授权彩猫查看相册")
sleep(2)
swipeUp(1000)
driver.find_element_by_accessibility_id("取消").click()
driver.find_element_by_accessibility_id("修改密码").click()
driver.find_element_by_accessibility_id("返回按钮").click()
driver.find_element_by_accessibility_id("返回按钮").click()
# 南交所资产
driver.find_element_by_accessibility_id("资产").click()
sleep(2)
try:
    driver.set_value(driver.find_element_by_accessibility_id("请输入交易密码"), '123456a')
    sleep(2)
except BaseException as e:
    print("已登录南交所账号")
else:
    driver.find_element_by_accessibility_id("登录").click()
sleep(3)
try:
    driver.find_element_by_accessibility_id("说明").click()
except BaseException as e:
    print("未成功跳转到南交所资产页面")
    driver.find_element_by_accessibility_id("返回按钮").click()
else:
    driver.find_element_by_accessibility_id("返回按钮").click()
    driver.find_element_by_accessibility_id("返回按钮").click()
# 交易所信息与变更
sleep(3)
driver.find_element_by_accessibility_id("交易所信息与变更").click()
sleep(3)
driver.find_element_by_accessibility_id("修改资金密码").click()
sleep(2)
driver.set_value(driver.find_element_by_accessibility_id("请输入当前资金密码"), '999999')
sleep(2)
driver.set_value(driver.find_element_by_accessibility_id("需为6位数字"), '111111')
driver.set_value(driver.find_element_by_accessibility_id("请再次输入"), '111112')
driver.find_element_by_accessibility_id("确定修改").click()
try:
    driver.find_element_by_accessibility_id("确定修改").click()
except BaseException as e:
    print("资金密码修改成功")
else:
    print("资金密码输入错误")
    sleep(2)
    driver.find_element_by_accessibility_id("返回按钮").click()
driver.find_element_by_accessibility_id("返回按钮").click()
# 消息提醒
driver.find_element_by_accessibility_id("消息提醒").click()
sleep(2)
driver.find_element_by_accessibility_id("成交提醒").click()
sleep(2)
driver.find_element_by_accessibility_id("查看详情").click()
try:
    driver.find_element_by_accessibility_id("委托单").click()
except BaseException as e:
    print("未成功跳转到我的订单页面")
else:
    print("成功跳转到我的订单页面")
driver.find_element_by_accessibility_id("返回按钮").click()
driver.find_element_by_accessibility_id("返回按钮").click()
sleep(2)
driver.find_element_by_accessibility_id("风险过高提醒").click()
sleep(2)
driver.find_element_by_accessibility_id("查看详情").click()
try:
    driver.find_element_by_accessibility_id("我的").click()
except BaseException as e:
    print("未成功跳转查看风险率")
else:
    print("成功跳转查看风险率")
sleep(2)
driver.find_element_by_accessibility_id("返回按钮").click()
sleep(2)
driver.find_element_by_accessibility_id("上涨提醒").click()
sleep(2)
driver.find_element_by_accessibility_id("返回按钮").click()
driver.find_element_by_accessibility_id("返回按钮").click()
# 新手学堂
driver.find_element_by_accessibility_id("新手学堂").click()
sleep(3)
driver.find_element_by_accessibility_id("第一课：为什么投资贵金属").click()
sleep(3)
swipLeft(1000)
swipLeft(1000)
sleep(2)
driver.find_element_by_accessibility_id("返回按钮").click()
sleep(2)
driver.find_element_by_accessibility_id("第二课：短线交易的6大法则").click()
sleep(3)
swipLeft(1000)
swipLeft(1000)
driver.find_element_by_accessibility_id("返回按钮").click()
driver.find_element_by_accessibility_id("返回按钮").click()
sleep(2)
# 帮助中心
driver.find_element_by_accessibility_id("帮助中心").click()
sleep(3)
swipeUp(1000)
sleep(2)
driver.find_element_by_accessibility_id("返回按钮").click()
sleep(2)
# 设置
driver.find_element_by_accessibility_id("设置").click()
driver.find_element_by_accessibility_id("开盘提醒, 今日开盘价").click()
sleep(2)
driver.find_element_by_accessibility_id("黑夜模式, 切换白天／黑夜两种模式").click()
sleep(2)
driver.find_element_by_accessibility_id("返回按钮").click()
sleep(2)
# 联系
driver.find_element_by_accessibility_id("联系客服").click()
sleep(2)
driver.find_element_by_accessibility_id("客服电话").click()
try:
    driver.find_element_by_accessibility_id("拨打热线 0574-87016757").click()
except BaseException as e:
    print("客服电话显示错误")
else:
    print("客服电话显示正确")
sleep(2)
driver.find_element_by_accessibility_id("取消").click()
sleep(2)
driver.find_element_by_accessibility_id("返回按钮").click()
swipeUp(1000)
# 关于
driver.find_element_by_accessibility_id("关于").click()
sleep(2)
driver.find_element_by_accessibility_id("箭头_向右").click()
sleep(3)
swipeUp(1000)
driver.find_element_by_accessibility_id("返回按钮").click()
driver.find_element_by_accessibility_id("返回按钮").click()
print("----我的模块测试结束----")







