from behave import use_fixture
from features.fixtures import browser_chrome



def before_all(context):
    pass

def before_feature(context):
    use_fixture(browser_chrome, context)



