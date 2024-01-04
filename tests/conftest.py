import os
import random

from dsl.pages.wp_dashboard import WPDashboardPage
from dsl.pages.wp_login import WPLoginPage
from dsl.pages.wp_plugins import WPPluginsPage
from helpers.utils import Settings as settings
import pytest
from playwright.sync_api import sync_playwright

from helpers.utils import load_yaml


@pytest.fixture(autouse=True)
def initiate_browser():
    p = sync_playwright().start()
    user_agent_strings = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2227.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.3497.92 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    ]
    ua = user_agent_strings[random.randint(0, len(user_agent_strings) - 1)]
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(user_agent=ua)

    # load yml files and save them in context
    load_yaml('../settings.yml')
    load_yaml('../locators.yml')
    settings.page = page

    return page


@pytest.fixture()
def plugin_setup_and_teardown():
    WPLoginPage().login_to_dashboard(username=settings.users['administrator']['username'],
                                     password=settings.users['administrator']['password'])
    dashboard = WPDashboardPage()
    dashboard.hover_over_menu_item(menu_item='Plugins ')
    plugins = WPPluginsPage()
    plugins.add_wp_crawler()
    plugins.activate_plugin()
    yield
    dashboard.select_menu_item(menu_item='Plugins ')
    plugins.deactivate_plugin()
    plugins.delete_plugin()
