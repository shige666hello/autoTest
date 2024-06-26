import ddt
import unittest
import os
from selenium import webdriver
import sys

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from util import log
from util.gettestdata import huoqu_test
from bussiness.functionPublic import Login_tes

path = os.getcwd()
case_path = os.path.join(path, 'data', 'case.xlsx')
casedata = huoqu_test(case_path, 3)

@ddt.ddt
class Testlogin(unittest.TestCase):
    def setUp(self):
        self.logs = log.log_message()
        self.derve = webdriver.Firefox()
        self.login_fun = Login_tes(self.derve)

    @ddt.data(*casedata)
    def test_login1(self, casedata):
        self.name = casedata['username']
        self.pwd = casedata['pwd']
        self.suc = casedata['suc']
        self.assert_value = casedata['assert']
        screenshot_path = os.path.join(path, 'resultpang', f"{self.name}_{self.pwd}.png")
        self.derve.get_screenshot_as_file(screenshot_path)
        self.logs.info_log(f'input data:name:{self.name},pwd:{self.pwd},suc:{self.suc},assert:{self.assert_value}')
        self.re_data = self.login_fun.login(self.suc, self.name, self.pwd)
        self.assertEqual(self.re_data, self.assert_value)

    def tearDown(self):
        self.derve.quit()

if __name__ == '__main__':
    unittest.main()
