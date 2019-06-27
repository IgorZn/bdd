import time, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from features.lib.basepage import BasePage


def get_binary_location():
    import getpass
    USER_NAME = getpass.getuser()
    PATH_APPDATA = 'C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\Application' % (USER_NAME)
    PATH_PF_x86 = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\"
    EXE_CHROME = "chrome.exe"

    if os.path.exists(PATH_APPDATA):
        for file in os.listdir(PATH_APPDATA):
            if file == EXE_CHROME:
                # print(os.path.join(PATH_APPDATA, file))
                binary_location = os.path.join(PATH_APPDATA, file)
                # print(binary_location)
                return binary_location
    else:
        binary_location = os.path.join(PATH_PF_x86, EXE_CHROME)
        # print(binary_location)
        return binary_location

chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.binary_location = get_binary_location()


def browser_chrome(context, timeout=30, **kwargs):
    # -- SETUP-FIXTURE PART:
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    context.browser = BasePage(browser)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    time.sleep(2)
    context.browser.close()
