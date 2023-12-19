from pytest_bdd import when
from helpers.utils import Settings as settings

from dsl.base_actions import BaseActions


@when("I navigate to indeed's url")
def navigate_to_homepage():
    BaseActions(page=settings.page).navigate_to_page(url=settings.urls['indeed']['home'])
