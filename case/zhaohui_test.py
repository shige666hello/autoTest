# -*- coding: utf-8 -*-
# @Author  : shige

from bussiness.functionPublic import Retrieve_tes
import unittest, time, os, ddt
from util import log
from selenium import webdriver
from util.gettestdata import fetch_test_cases

# 获取当前工作目录
path = os.getcwd()
# 测试用例文件路径
case_path = path + '\\data\\case.xlsx'
# 获取测试用例数据
casedata = fetch_test_cases(case_path, 2)

@ddt.ddt
class Testzhaohui(unittest.TestCase):
    def setUp(self):
        self.logs = log.LogMessage()  # 初始化日志记录工具
        self.derve = webdriver.Firefox()  # 初始化浏览器驱动
        self.zhaohui_fun = Retrieve_tes(self.derve)  # 初始化找回密码功能对象

    @ddt.data(*casedata)
    def test_zhaohui_1(self, casedata):
        # 从测试用例数据中获取用户名、邮箱、成功标志和断言值
        self.username = casedata['username']
        self.email = casedata['email']
        self.suc = casedata['suc']
        self.assert_vale = casedata['assert_vale']

        # 执行找回密码操作并获取返回数据
        self.retu_data = self.zhaohui_fun.zhaohui(self.suc, self.username, self.email)
        
        # 截取截图并保存到指定路径
        self.derve.get_screenshot_as_file(path + '\\resultpang\\%s.png' % casedata['id'])
        
        # 记录输入数据到日志
        self.logs.info_log('input name:%s, email:%s, assert:%s' % (self.username, self.email, self.assert_vale))
        
        time.sleep(1)
        
        # 断言找回密码结果与预期值是否相等
        self.assertEqual(self.retu_data, self.assert_vale)

    def tearDown(self):
        self.derve.quit()  # 关闭浏览器