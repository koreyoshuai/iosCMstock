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

sleep(2)
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
    y1 = int(l[1] * 0.7)  # 起始y坐标
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
    driver.swipe(x1, 0,x2-x1, 0, t)

# 屏幕向右滑动
def swipRight(t):
    l = getSize()
    x1 = int(l[0] * 0.05)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    driver.swipe(x1, 0, x2-x1, 0, t)

sleep(3)
driver.find_element_by_accessibility_id("交易").click()
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
try:
    driver.find_element_by_accessibility_id("取消").click()
except BaseException as e:
    pass
else:
    pass
sleep(3)
try:
    driver.find_element_by_accessibility_id("买入").click()
except BaseException as e:
    print(e)
else:
    print("成功登录交易页面")
# 跳转到行情
sleep(2)
driver.find_element_by_accessibility_id("交易_走势图").click()
sleep(3)
try:
    driver.find_element_by_accessibility_id("back icon").click()
except BaseException as e:
    print("跳转到行情失败")
else:
    print("成功跳转到行情页面")
# 买入和卖出
sleep(2)
driver.find_element_by_accessibility_id("白银 AG").click()
driver.find_element_by_accessibility_id("确定").click()
sleep(2)
driver.find_element_by_accessibility_id("限价买入").click()
sleep(2)
driver.find_element_by_accessibility_id("市价快速买入").click()
driver.find_element_by_accessibility_id("加号 橙").click()
sleep(2)
def mairu():
    l = getSize()
    x1 = int(l[0] * 0.27)
    y1 = int(l[1] * 0.57)
    TouchAction(driver).tap(None,x1,y1).perform()
mairu()
try:
    driver.find_element_by_accessibility_id("确定买入").click()
except BaseException as e:
    print("当前账号资金不足")
    driver.find_element_by_accessibility_id("立即转账").click()
else:
    print("成功购买白银")
sleep(2)
driver.find_element_by_accessibility_id("卖出").click()
sleep(2)
driver.find_element_by_accessibility_id("如何用5档？").click()
sleep(3)
swipeUp(1000)
driver.find_element_by_accessibility_id("返回按钮").click()
sleep(2)
driver.find_element_by_accessibility_id("限价卖出").click()
sleep(2)
driver.find_element_by_accessibility_id("满足条件卖出").click()
sleep(2)


# 止盈止损
driver.find_element_by_accessibility_id("持仓").click()
sleep(2)
try:
    driver.find_element_by_accessibility_id("快速平仓").click()
except BaseException as e:
    print("当前无持仓")
else:
    sleep(2)
    driver.find_element_by_accessibility_id("取消").click()
    driver.find_element_by_accessibility_id("平仓").click()
    swipRight(1000)
    try:
        driver.find_element_by_accessibility_id("卖出价格").click()
    except BaseException as e:
        pass
    else:
        pass
    sleep(2)
    swipeUp(1000)
    driver.find_element_by_accessibility_id("成交单").click()
    sleep(2)
    driver.find_element_by_accessibility_id("委托单").click()
    sleep(3)
    driver.find_element_by_accessibility_id("返回按钮").click()
    try:
        driver.find_element_by_accessibility_id("撤单").click()
    except BaseException as e:
        print("平仓设置失败")
    else:
        print("平仓设置成功")
        driver.find_element_by_accessibility_id("取消").click()
sleep(2)
driver.find_element_by_accessibility_id("止盈止损").click()
sleep(2)
driver.find_element_by_accessibility_id("对号 蓝色").click()
sleep(2)
driver.find_element_by_accessibility_id("我的 消息提醒 蓝色").click()
driver.find_element_by_accessibility_id("达到以上条件时提醒我").click()
sleep(2)
driver.find_element_by_accessibility_id("圆圈 灰色").click()
driver.find_element_by_accessibility_id("确定设置").click()
sleep(2)
driver.find_element_by_accessibility_id("确定").click()
sleep(2)
swipeUp(1000)
try:
    driver.find_element_by_accessibility_id("撤单").click()
except BaseException as e:
    print("添加止盈止损单失败")
else:
    driver.find_element_by_accessibility_id("确定").click()
    sleep(2)
    driver.find_element_by_accessibility_id("查看").click()
    sleep(2)
    driver.find_element_by_accessibility_id("确定").click()
sleep(2)
driver.find_element_by_accessibility_id("规则").click()
sleep(3)
driver.find_element_by_accessibility_id("返回按钮").click()
sleep(2)
driver.find_element_by_accessibility_id("返回按钮").click()

# 成交单和委托单
sleep(3)
driver.find_element_by_accessibility_id("成交单").click()
driver.find_element_by_accessibility_id("返回按钮").click()

#持仓
sleep(2)
driver.find_element_by_accessibility_id("可用资金").click()
sleep(2)
driver.find_element_by_accessibility_id("说明").click()
sleep(2)
driver.find_element_by_accessibility_id("返回按钮").click()
driver.find_element_by_accessibility_id("更多 >").click()
sleep(2)
swipeUp(1000)
sleep(2)
driver.find_element_by_accessibility_id("融货费").click()
sleep(2)
driver.find_element_by_accessibility_id("返回按钮").click()
swipeUp(1000)
sleep(2)
driver.find_element_by_accessibility_id("转入/转出资金").click()
try:
    driver.find_element_by_accessibility_id("建议转入100.00元以上金额").click()
except BaseException as e:
    print("未成功跳转到转账页面")
else:
    print("成功跳转到转账页面")
    driver.set_value(driver.find_element_by_accessibility_id("建议转入100.00元以上金额"),"1")
    sleep(2)
    driver.find_element_by_accessibility_id("确定转入").click()
    sleep(3)
    driver.set_value(driver.find_element_by_accessibility_id("输入密码_无密码"), "111111")
    sleep(2)
    try:
        driver.find_element_by_accessibility_id("确定").click()
    except BaseException as e:
        print("密码正确已转入成功")
    else:
        print("密码错误")
    sleep(2)
    driver.find_element_by_accessibility_id("delete zx").click()
    sleep(2)
    driver.find_element_by_accessibility_id("为什么我不能转入？").click()
    sleep(2)
    driver.find_element_by_accessibility_id("返回按钮").click()
    sleep(2)
    driver.find_element_by_accessibility_id("转账查询").click()
    sleep(2)
    driver.find_element_by_accessibility_id("查询历史转账记录").click()
    sleep(2)
    driver.find_element_by_accessibility_id("箭头_向下").click()
    sleep(2)
    driver.find_element_by_accessibility_id("确 定").click()
    driver.find_element_by_accessibility_id("返回按钮").click()
    sleep(2)
    driver.find_element_by_accessibility_id("助手").click()
    driver.find_element_by_accessibility_id("意见反馈").click()
    sleep(2)
    driver.find_element_by_accessibility_id("返回按钮").click()
sleep(2)
print("----交易模块测试结束-----")











