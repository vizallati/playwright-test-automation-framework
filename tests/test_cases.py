from pytest_bdd import scenario
from steps.when import *
from steps.then import *


@scenario('features/home_page.feature', 'Navigate to Homepage')
def test_home_page():
    pass