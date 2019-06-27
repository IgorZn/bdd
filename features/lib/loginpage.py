from selenium.webdriver.common.by import By

class LoginPage:
    locators = {
        "login": (By.XPATH, "(//input[@name='session[username_or_email]'])[1]"),
        "password": (By.XPATH, "(//input[@name='session[password]'])[1]"),
        "submit": (By.XPATH, "(//input[@class='EdgeButton EdgeButton--secondary EdgeButton--medium submit js-submit'])[1]"),
        "error_message": 'The email and password you entered did not match our records. Please double-check and try again.'
    }
