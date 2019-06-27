from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from features.lib.basepage import BasePage



chrome_options = Options()

def browser_chrome(context):
    # -- SETUP-FIXTURE PART:
    browser = webdriver.Chrome()
    context.browser = BasePage(browser)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.close()