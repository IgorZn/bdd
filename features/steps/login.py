from behave import given, when, then
from features.lib.loginpage import LoginPage

@given('Open {url}')
def step_impl(context, url):
    assert url in context.browser.get_url


@when('send login {login}, password {password} and log in')
def step_impl(context, login, password):
    loginpage = LoginPage()
    context.browser.find_element_wait(loginpage.locators['password']).send_keys(password)
    context.browser.find_element_wait(loginpage.locators['login']).send_keys(login)
    context.browser.find_element_wait(loginpage.locators['submit']).click()


@then(u'a login error message should display')
def step_impl(context):
    message = context.browser.contains_content(
        LoginPage.locator_dictionary['error_message'], 5)
    assert message



@then(u'the user should be redirected to homepage')
def step_impl(context):
    pass