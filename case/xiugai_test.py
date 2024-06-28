# -*- coding: utf-8 -*-
# @Author  : shige
from bussiness.functionPublic import ChangePwd_tes  # 导入修改密码功能类
from selenium import webdriver
import unittest
import time
import os
import ddt
from util import log
from util.gettestdata import fetch_test_cases

path = os.getcwd()
case_path = os.path.join(path, 'data', 'case.xlsx')
casedata = fetch_test_cases(case_path, 3)

@ddt.ddt
class Test_xiugai(unittest.TestCase):
    def setUp(self):
        self.logs = log.LogMessage()
        self.driver = webdriver.Firefox()
        self.xiugai_fun = ChangePwd_tes(self.driver)  # 使用修改密码功能类

    @ddt.data(*casedata)
    def test_xiugai_1(self, casedata):
        # 从测试用例数据中获取当前密码、新密码、确认新密码、成功标志和断言值
        self.current_pwd = casedata['current_pwd']
        self.new_pwd = casedata['new_pwd']
        self.confirm_pwd = casedata['confirm_pwd']
        self.suc = casedata['suc']
        self.assert_value = casedata['assert_value']
        # 执行修改密码操作并获取结果数据
        self.return_data = self.xiugai_fun.change_password(self.suc, self.current_pwd, self.new_pwd, self.confirm_pwd)
        # 记录输入的数据
        self.logs.info_log("输入数据: 当前密码:%s, 新密码:%s, 确认新密码:%s, 断言:%s" % (self.current_pwd, self.new_pwd, self.confirm_pwd, self.assert_value))
        # 等待1秒
        time.sleep(1)
        # 断言结果数据是否与预期值一致
        self.assertAlmostEqual(self.return_data, self.assert_value)

    def tearDown(self):
        # 关闭浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
