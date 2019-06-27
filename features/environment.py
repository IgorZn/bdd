from behave import use_fixture
from features.fixtures import browser_chrome



def before_all(context):
    pass

def before_feature(context, feature):
    use_fixture(browser_chrome, context)

def after_scenario(context, scenario):
    context.browser.screenshot(scenario)

def after_all(context):
    print("===== That's all folks =====")




