from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class WebDriverWrapper:
    def __init__(self, browser):
        if browser.lower() in ['firefox', 'f']:
            self.driver = webdriver.Firefox()
        elif browser.lower() in ['ie', 'i']:
            self.driver = webdriver.Ie()
        elif browser.lower() in ['chrome', 'ch']:
            self.driver = webdriver.Chrome()
        elif browser.lower() in ['edge', 'ed']:
            self.driver = webdriver.Edge()
        elif browser.lower() in ['safari', 'sa']:
            self.driver = webdriver.Safari()
        else:
            raise NameError('Unsupported browser. Please choose from: Firefox, IE, Chrome, PhantomJS, Edge, Opera, Safari')

    def find_element(self, locator_type, locator):
        if locator_type == 'id':
            return self.driver.find_element(By.ID, locator)
        elif locator_type == 'name':
            return self.driver.find_element(By.NAME, locator)
        elif locator_type == 'class':
            return self.driver.find_element(By.CLASS_NAME, locator)
        elif locator_type == 'link_text':
            return self.driver.find_element(By.LINK_TEXT, locator)
        elif locator_type == 'xpath':
            return self.driver.find_element(By.XPATH, locator)
        elif locator_type == 'tag':
            return self.driver.find_element(By.TAG_NAME, locator)
        elif locator_type == 'css':
            return self.driver.find_element(By.CSS_SELECTOR, locator)
        else:
            raise ValueError("Invalid locator type. Supported types: 'id', 'name', 'class', 'link_text', 'xpath', 'css', 'tag'")

    def find_elements(self, locator_type, locator):
        if locator_type == 'id':
            return self.driver.find_elements(By.ID, locator)
        elif locator_type == 'name':
            return self.driver.find_elements(By.NAME, locator)
        elif locator_type == 'class':
            return self.driver.find_elements(By.CLASS_NAME, locator)
        elif locator_type == 'link_text':
            return self.driver.find_elements(By.LINK_TEXT, locator)
        elif locator_type == 'xpath':
            return self.driver.find_elements(By.XPATH, locator)
        elif locator_type == 'tag':
            return self.driver.find_elements(By.TAG_NAME, locator)
        elif locator_type == 'css':
            return self.driver.find_elements(By.CSS_SELECTOR, locator)
        else:
            raise ValueError("Invalid locator type. Supported types: 'id', 'name', 'class', 'link_text', 'xpath', 'css', 'tag'")

    def wait_for_element(self, locator_type, locator, timeout=10):
        if locator_type == 'id':
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, locator)))
        elif locator_type == 'name':
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.NAME, locator)))
        elif locator_type == 'class':
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, locator)))
        elif locator_type == 'link_text':
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.LINK_TEXT, locator)))
        elif locator_type == 'xpath':
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
        elif locator_type == 'css':
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        else:
            raise ValueError("Invalid locator type. Supported types: 'id', 'name', 'class', 'link_text', 'xpath', 'css'")

    def open_url(self, url):
        self.driver.get(url)

    def maximize_window(self):
        self.driver.maximize_window()

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def send_keys_to_element(self, locator_type, locator, text):
        element = self.find_element(locator_type, locator)
        element.clear()
        element.send_keys(text)

    def clear_element(self, locator_type, locator):
        element = self.find_element(locator_type, locator)
        element.clear()

    def click_element(self, locator_type, locator):
        element = self.find_element(locator_type, locator)
        element.click()

    def right_click_element(self, locator_type, locator):
        element = self.find_element(locator_type, locator)
        ActionChains(self.driver).context_click(element).perform()

    def move_to_element(self, locator_type, locator):
        element = self.find_element(locator_type, locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click_element(self, locator_type, locator):
        element = self.find_element(locator_type, locator)
        ActionChains(self.driver).double_click(element).perform()

    def drag_and_drop(self, locator_type1, locator1, locator_type2, locator2):
        source_element = self.find_element(locator_type1, locator1)
        target_element = self.find_element(locator_type2, locator2)
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    def click_link_text(self, text):
        self.driver.find_element(By.LINK_TEXT, text).click()

    def close_browser(self):
        self.driver.close()

    def quit_browser(self):
        self.driver.quit()

    def submit_form(self, locator_type, locator):
        element = self.find_element(locator_type, locator)
        element.submit()

    def refresh_page(self):
        self.driver.refresh()

    def execute_js(self, script):
        self.driver.execute_script(script)

    def get_attribute(self, locator_type, locator, attribute):
        element = self.find_element(locator_type, locator)
        return element.get_attribute(attribute)

    def get_text(self, locator_type, locator):
        element = self.find_element(locator_type, locator)
        return element.text

    def is_element_displayed(self, locator_type, locator):
        element = self.find_element(locator_type, locator)
        return element.is_displayed()

    def get_page_title(self):
        return self.driver.title

    def take_screenshot(self, file_path):
        self.driver.get_screenshot_as_file(file_path)

    def implicitly_wait(self, time_to_wait):
        self.driver.implicitly_wait(time_to_wait)

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, locator_type, locator):
        frame_element = self.find_element(locator_type, locator)
        self.driver.switch_to.frame(frame_element)
