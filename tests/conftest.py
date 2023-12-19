import random
from helpers.utils import Settings as settings
import pytest
from playwright.sync_api import sync_playwright

from helpers.utils import load_yaml, yaml_files


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
    # Switched browser to firefox, because chromium does not support use of proxy server
    browser = p.firefox.launch(headless=False)
    page = browser.new_page(user_agent=ua)

    # load yml files and save them in context
    load_yaml('../settings.yml')
    load_yaml('../locators.yml')
    settings.page = page

    return page
