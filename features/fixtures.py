import time, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from features.lib.basepage import BasePage

chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("--no-sandbox")


def browser_chrome(context, timeout=30, **kwargs):
    # -- SETUP-FIXTURE PART:
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    context.browser = BasePage(browser)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    time.sleep(2)
    context.browser.close()
