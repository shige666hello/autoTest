import os
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util import log

path = os.getcwd()

class Login_tes:
    def __init__(self, driver):
        self.driver = driver
        self.logs = log.log_message()
        self.load_data()

    def load_data(self):
        with open(os.path.join(path, "data", "page_data.yaml"), "r", encoding="utf-8") as file:
            self.data = yaml.safe_load(file)['login']
            self.lo_url = self.data.get('url')
            self.log_in = self.data.get('log_in')
            self.username = self.data.get('name')
            self.password = self.data.get('password')
            self.sub = self.data.get('log_in_btm')
            self.lo_err = self.data.get('login_err')
            self.lo_suc = self.data.get('login_suc')

    def login(self, suc, name, password):
        try:
            self.driver.get(self.lo_url)
            self.driver.find_element(By.LINK_TEXT, self.log_in).click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, self.username)))
            self.driver.find_element(By.ID, self.username).clear()
            self.driver.find_element(By.ID, self.username).send_keys(name)
            self.driver.find_element(By.ID, self.password).click()
            self.driver.find_element(By.ID, self.password).send_keys(password)
            self.driver.find_element(By.ID, self.sub).click()

            if suc == '1':
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.lo_suc)))
                return self.driver.find_element(By.XPATH, self.lo_suc).text
            elif suc == '0':
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.lo_err)))
                return self.driver.find_element(By.XPATH, self.lo_err).text

        except Exception as e:
            self.logs.error_log(f'用例执行失败，原因：{e}')

        finally:
            self.driver.quit()

class Zhuce_tes:
    def __init__(self, driver):
        self.driver = driver
        self.logs = log.log_message()
        self.load_data()

    def load_data(self):
        with open(os.path.join(path, "data", "page_data.yaml"), "r", encoding="utf-8") as file:
            self.data = yaml.safe_load(file)['zhuce']
            self.zhu_url = self.data.get('url')
            self.zhu = self.data.get('zhuc')
            self.zhu_user = self.data.get('username')
            self.zhu_pwd = self.data.get('password')
            self.zhu_qpwd = self.data.get('querenpass')
            self.zhu_shouji = self.data.get('shouji')
            self.zhu_email = self.data.get('youxiang')
            self.zhu_butn = self.data.get('tijiao_btn')
            self.zhu_suc = self.data.get('zhuce_suc')
            self.zhu_err = self.data.get('zhuce_err')

    def zhuce(self, suc, name, password, password1, shouji, email):
        try:
            self.driver.get(self.zhu_url)
            self.driver.find_element(By.LINK_TEXT, self.zhu).click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, self.zhu_user)))
            self.driver.find_element(By.CLASS_NAME, self.zhu_user).clear()
            self.driver.find_element(By.CLASS_NAME, self.zhu_user).send_keys(name)
            self.driver.find_element(By.CLASS_NAME, self.zhu_pwd).clear()
            self.driver.find_element(By.CLASS_NAME, self.zhu_pwd).send_keys(password)
            self.driver.find_element(By.CLASS_NAME, self.zhu_qpwd).clear()
            self.driver.find_element(By.CLASS_NAME, self.zhu_qpwd).send_keys(password1)
            self.driver.find_element(By.CLASS_NAME, self.zhu_shouji).clear()
            self.driver.find_element(By.CLASS_NAME, self.zhu_shouji).send_keys(shouji)
            self.driver.find_element(By.CLASS_NAME, self.zhu_email).clear()
            self.driver.find_element(By.CLASS_NAME, self.zhu_email).send_keys(email)
            self.driver.find_element(By.CLASS_NAME, self.zhu_butn).click()

            if suc == "1":
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.ID, self.zhu_suc)))
                return self.driver.find_element(By.ID, self.zhu_suc).text
            elif suc == '0':
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.zhu_err)))
                return self.driver.find_element(By.XPATH, self.zhu_err).text

        except Exception as e:
            self.logs.error_log(f'用例执行失败，原因：{e}')

        finally:
            self.driver.quit()

class Zaohui_tes:
    def __init__(self, driver):
        self.driver = driver
        self.logs = log.log_message()
        self.load_data()

    def load_data(self):
        with open(os.path.join(path, "data", "page_data.yaml"), "r", encoding="utf-8") as file:
            self.data = yaml.safe_load(file)['zhaohui']
            self.zhao_url = self.data.get('url')
            self.zhao_username = self.data.get('username')
            self.zhao_btn = self.data.get('zhaohui_btn')
            self.zhao_err = self.data.get('zhaohui_err')
            self.zhao_suc = self.data.get('zhaohui_suc')

    def zhaohui(self, suc, name, email):
        try:
            self.driver.get(self.zhao_url)
            self.driver.find_element(By.CSS_SELECTOR, self.zhao_username).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.zhao_username).send_keys(name)
            self.driver.find_element(By.CSS_SELECTOR, self.zhao_email).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.zhao_email).send_keys(email)
            self.driver.find_element(By.CSS_SELECTOR, self.zhao_btn).click()

            if suc == '1':
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, self.zhao_suc)))
                return self.driver.find_element(By.CSS_SELECTOR, self.zhao_suc).text
            elif suc == "0":
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.zhao_err)))
                return self.driver.find_element(By.XPATH, self.zhao_err).text

        except Exception as e:
            self.logs.error_log(f'用例执行失败，原因：{e}')

        finally:
            self.driver.quit()

class Rest_tes:
    def __init__(self, driver):
        self.driver = driver
        self.logs = log.log_message()
        self.load_data()

    def load_data(self):
        with open(os.path.join(path, "data", "page_data.yaml"), "r", encoding="utf-8") as file:
            self.data = yaml.safe_load(file)['reset_pwd']
            self.rest_url = self.data.get('url')
            self.rest_email = self.data.get('email')
            self.reset_yan = self.data.get('yanzheng')
            self.reset_password = self.data.get('password')
            self.reset_passwordque = self.data.get('chongzhipassword')
            self.reset_btn = self.data.get('reset_btn')
            self.reset_error = self.data.get('reset_error')
            self.reset_suc = self.data.get('reset_suc')

    def rest(self, suc, yan, email, password, chongzhipassword):
        try:
            self.driver.get(self.rest_url)
            self.driver.find_element(By.CSS_SELECTOR, self.rest_email).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.rest_email).send_keys(email)
            self.driver.find_element(By.CSS_SELECTOR, self.reset_yan).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.reset_yan).send_keys(yan)
            self.driver.find_element(By.CSS_SELECTOR, self.reset_password).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.reset_password).send_keys(password)
            self.driver.find_element(By.CSS_SELECTOR, self.reset_passwordque).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.reset_passwordque).send_keys(chongzhipassword)
            self.driver.find_element(By.CSS_SELECTOR, self.reset_btn).click()

            if suc == "1":
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.ID, self.reset_suc)))
                return self.driver.find_element(By.ID, self.reset_suc).text
            elif suc == '0':
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.reset_error)))
                return self.driver.find_element(By.XPATH, self.reset_error).text

        except Exception as e:
            self.logs.error_log(f'用例执行失败，原因：{e}')

        finally:
            self.driver.quit()

