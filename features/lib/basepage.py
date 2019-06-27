from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import traceback
import time

class BasePage(object):

    def __init__(self, browser, base_url='http://twitter.com/'):
        self.base_url = base_url
        self.browser = browser
        self._web_driver_wait = WebDriverWait(browser, self.timeout)
        self.timeout = 30

    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    def find_element_wait(self, *locator):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, locator[1])))

    def visit(self, url):
        self.browser.get(url)

    def hover(self, element):
            ActionChains(self.browser).move_to_element(element).perform()
            time.sleep(5)

