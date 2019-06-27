from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import traceback
import time, os

class BasePage(object):
    __TIMEOUT = 10

    def __init__(self, browser, base_url='http://twitter.com/'):
        self.base_url = base_url
        self.browser = browser
        self._web_driver_wait = WebDriverWait(browser, self.__TIMEOUT)
        self.timeout = 30
        self.start()

    def start(self):
        self.browser.implicitly_wait(10)
        self.browser.get(self.base_url)

    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    def find_element_wait(self, *locator):
        try:
            return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, self.get_value(*locator))))
        except TimeoutException:
            self.browser.save_screenshot('.'+os.sep+os.getcwd()+os.sep+'error.png')

    def visit(self, url):
        self.browser.get(url)

    def hover(self, element):
            ActionChains(self.browser).move_to_element(element).perform()
            time.sleep(5)

    def close(self):
        self.browser.close()

    @property
    def get_url(self):
        return self.browser.current_url

    def get_title(self):
        return self.browser.title

    def get_value(self, locator):
        return locator[1]

    def screenshot(self, filename):
        self.browser.save_screenshot('screenie.png')

