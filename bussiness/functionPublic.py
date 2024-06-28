import os
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util import log
from util import WebDriverWrapper

class Login_tes:
    def __init__(self, driver):
        self.driver = driver
        self.logs = log.LogMessage()
        self.load_data()

    def load_data(self):
        path = os.getcwd()
        with open(os.path.join(path, "data", "page_data.yaml"), "r", encoding="utf-8") as file:
            self.data = yaml.safe_load(file)['login']
            self.lo_url = self.data.get('url')
            self.log_in = self.data.get('log_in')
            self.username = self.data.get('name')
            self.password = self.data.get('password')
            self.sub = self.data.get('log_in_btn')
            self.lo_err = self.data.get('login_err')
            self.lo_suc = self.data.get('login_suc')

    def login(self, suc, name, password):
        try:
            wrapper = WebDriverWrapper(self.driver)
            wrapper.open_url(self.lo_url)
            wrapper.click_link_text(self.log_in)
            wrapper.wait_for_element('id', self.username)
            wrapper.send_keys_to_element('id', self.username, name)
            wrapper.send_keys_to_element('id', self.password, password)
            wrapper.click_element('id', self.sub)

            if suc == '1':
                wrapper.wait_for_element('xpath', self.lo_suc)
                return wrapper.get_text('xpath', self.lo_suc)
            elif suc == '0':
                wrapper.wait_for_element('xpath', self.lo_err)
                return wrapper.get_text('xpath', self.lo_err)

        except Exception as e:
            self.logs.error_log(f'用例执行失败，原因：{e}')

        finally:
            wrapper.quit_browser()

class sign_in_tes:
    def __init__(self, driver):
        self.driver = driver
        self.logs = log.LogMessage()
        self.load_data()

    def load_data(self):
        path = os.getcwd()
        with open(os.path.join(path, "data", "page_data.yaml"), "r", encoding="utf-8") as file:
            self.data = yaml.safe_load(file)['sign_in']
            self.zhu_url = self.data.get('url')
            self.zhu = self.data.get('zhuce')
            self.zhu_user = self.data.get('username')
            self.zhu_pwd = self.data.get('password')
            self.zhu_qpwd = self.data.get('querenpass')
            self.zhu_shouji = self.data.get('shouji')
            self.zhu_email = self.data.get('youxiang')
            self.zhu_butn = self.data.get('tijiao_btn')
            self.zhu_suc = self.data.get('sign_in_suc')
            self.zhu_err = self.data.get('sign_in_err')

    def sign_in(self, suc, name, password, password1, shouji, email):
        try:
            wrapper = WebDriverWrapper(self.driver)
            wrapper.open_url(self.zhu_url)
            wrapper.click_link_text(self.zhu)
            wrapper.wait_for_element('class', self.zhu_user)
            wrapper.send_keys_to_element('class', self.zhu_user, name)
            wrapper.send_keys_to_element('class', self.zhu_pwd, password)
            wrapper.send_keys_to_element('class', self.zhu_qpwd, password1)
            wrapper.send_keys_to_element('class', self.zhu_shouji, shouji)
            wrapper.send_keys_to_element('class', self.zhu_email, email)
            wrapper.click_element('class', self.zhu_butn)

            if suc == '1':
                wrapper.wait_for_element('id', self.zhu_suc)
                return wrapper.get_text('id', self.zhu_suc)
            elif suc == '0':
                wrapper.wait_for_element('xpath', self.zhu_err)
                return wrapper.get_text('xpath', self.zhu_err)

        except Exception as e:
            self.logs.error_log(f'用例执行失败，原因：{e}')

        finally:
            wrapper.quit_browser()


class Retrieve_tes:
    def __init__(self, driver):
        self.driver = driver
        self.logs = log.LogMessage()
        self.load_data()

    def load_data(self):
        path = os.getcwd()
        with open(os.path.join(path, "data", "page_data.yaml"), "r", encoding="utf-8") as file:
            self.data = yaml.safe_load(file)['zhaohui']
            self.zhao_url = self.data.get('url')
            self.zhao_username = self.data.get('username')
            self.zhao_email = self.data.get('youxiang')
            self.zhao_btn = self.data.get('zhaohui_btn')
            self.zhao_err = self.data.get('zhaohui_err')
            self.zhao_suc = self.data.get('zhaohui_suc')

    def zhaohui(self, suc, name, email):
        try:
            wrapper = WebDriverWrapper(self.driver)
            wrapper.open_url(self.zhao_url)
            wrapper.send_keys_to_element('css', self.zhao_username, name)
            wrapper.send_keys_to_element('css', self.zhao_email, email)
            wrapper.click_element('css', self.zhao_btn)

            if suc == '1':
                wrapper.wait_for_element('css', self.zhao_suc)
                return wrapper.get_text('css', self.zhao_suc)
            elif suc == '0':
                wrapper.wait_for_element('xpath', self.zhao_err)
                return wrapper.get_text('xpath', self.zhao_err)

        except Exception as e:
            self.logs.error_log(f'用例执行失败，原因：{e}')

        finally:
            wrapper.quit_browser()


class ChangePwd_tes:
    def __init__(self, driver):
        self.driver = driver
        self.logs = log.LogMessage()
        self.load_data()

    def load_data(self):
        path = os.getcwd()
        with open(os.path.join(path, "data", "page_data.yaml"), "r", encoding="utf-8") as file:
            self.data = yaml.safe_load(file)['change_pwd']
            self.change_url = self.data.get('url')
            self.current_pwd = self.data.get('current_pwd')
            self.new_pwd = self.data.get('new_pwd')
            self.confirm_pwd = self.data.get('confirm_pwd')
            self.change_btn = self.data.get('change_btn')
            self.change_error = self.data.get('change_error')
            self.change_suc = self.data.get('change_suc')

    def change_password(self, suc, current_pwd, new_pwd, confirm_pwd):
        try:
            wrapper = WebDriverWrapper(self.driver)
            wrapper.open_url(self.change_url)
            wrapper.send_keys_to_element('css', self.current_pwd, current_pwd)
            wrapper.send_keys_to_element('css', self.new_pwd, new_pwd)
            wrapper.send_keys_to_element('css', self.confirm_pwd, confirm_pwd)
            wrapper.click_element('css', self.change_btn)

            if suc == '1':
                wrapper.wait_for_element('id', self.change_suc)
                return wrapper.get_text('id', self.change_suc)
            elif suc == '0':
                wrapper.wait_for_element('xpath', self.change_error)
                return wrapper.get_text('xpath', self.change_error)

        except Exception as e:
            self.logs.error_log(f'用例执行失败，原因：{e}')

        finally:
            wrapper.quit_browser()
