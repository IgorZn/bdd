from behave import given, when, then
from features.lib.loginpage import LoginPage

@given('Open {url}')
def visit_login(context, url):
    context.browser.visit(url)


@when('send login {login}, password {password} and log in')
def login(context, login, password):
    loginpage = LoginPage()
    context.browser.find_element(loginpage.locators['password']).send_keys(password)
    context.browser.find_element(loginpage.locators['login']).send_keys(login)
    context.browser.find_element(loginpage.locators['submit']).click()



@then(u'a login error message should display')
def step_impl(context):
    message = context.browser.contains_content(
        LoginPage.locator_dictionary['error_message'], 5)
    assert message



@then(u'the user should be redirected to homepage')
def homepage(context):
    home = context.browser.contains_content(USER['valid']['username'], 10)
    assert home