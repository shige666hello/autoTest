# -*- coding: utf-8 -*-
# @Author  : shige
from bussiness.functionPublic import sign_in_tes
import unittest, time, os, ddt
from util import log
from selenium import webdriver
from util.gettestdata import fetch_test_cases

path = os.getcwd()
case_path = os.path.join(path, 'data', 'case.xlsx')
casedata = fetch_test_cases(case_path, 1)

@ddt.ddt
class Testsign_in(unittest.TestCase):
    def setUp(self):
        self.logs = log.LogMessage()
        self.driver = webdriver.Firefox()
        self.sign_in_fun = sign_in_tes(self.driver)

    @ddt.data(*casedata)
    def test_sign_in_1(self, casedata):
        self.name = casedata['username']
        self.password = casedata['password']
        self.passwordque = casedata['mima2']
        self.shoujihao = casedata['shoujihao']
        self.youxiang = casedata['youxiang']
        self.suc = casedata['suc']
        self.assert_vale = casedata['assert_vale']

        self.re_data = self.sign_in_fun.sign_in(self.suc, self.name, self.password, self.passwordque, self.shoujihao, self.youxiang)
        
        screenshot_path = os.path.join(path, 'resultpng', f"{casedata['id']}.png")
        self.driver.get_screenshot_as_file(screenshot_path)
        
        self.logs.info_log(f"input: name:{self.name}, password:{self.password}, passwordque:{self.passwordque}, shoujihao:{self.shoujihao}, youxiang:{self.youxiang}, assert:{self.assert_vale}")
        time.sleep(1)
        self.assertEqual(self.re_data, self.assert_vale)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
