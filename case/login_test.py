import ddt
import unittest
import os
from selenium import webdriver
import sys

# 将父目录添加到 sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from util import log
from util.gettestdata import fetch_test_cases
from bussiness.functionPublic import Login_tes

# 获取当前工作目录路径
path = os.getcwd()
# 测试用例文件路径
case_path = os.path.join(path, 'data', 'case.xlsx')
# 获取测试用例数据
casedata = fetch_test_cases(case_path, 0)

# 使用ddt数据驱动测试
@ddt.ddt
class Testlogin(unittest.TestCase):
    def setUp(self):
        # 初始化日志记录工具
        self.logs = log.LogMessage()
        # 使用谷歌浏览器
        self.driver = webdriver.Chrome()
        # 初始化登录功能类
        self.login_fun = Login_tes(self.driver)

    @ddt.data(*casedata)
    def test_login1(self, casedata):
        # 从测试用例数据中获取用户名、密码、成功标志和断言值
        self.name = casedata['username']
        self.pwd = casedata['pwd']
        self.suc = casedata['suc']
        self.assert_value = casedata['assert']
        # 截图保存路径
        screenshot_path = os.path.join(path, 'resultpang', f"{self.name}_{self.pwd}.png")
        # 获取登录页面的截图
        self.driver.get_screenshot_as_file(screenshot_path)
        # 记录输入的数据
        self.logs.info_log(f'输入数据: 用户名:{self.name}, 密码:{self.pwd}, 成功标志:{self.suc}, 断言:{self.assert_value}')
        # 执行登录操作并获取结果数据
        self.re_data = self.login_fun.login(self.suc, self.name, self.pwd)
        # 断言结果数据是否与预期值一致
        self.assertEqual(self.re_data, self.assert_value)

    def tearDown(self):
        # 关闭浏览器
        self.driver.quit()

if __name__ == '__main__':
    # 运行测试用例
    unittest.main()
