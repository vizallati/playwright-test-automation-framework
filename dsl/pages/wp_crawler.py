from dsl.base_actions import BaseActions
from helpers.utils import Settings as settings, yaml_files, get_absolute_path, load_yaml


class WPCrawlerPage(BaseActions):
    def __init__(self):
        super().__init__(settings.page)
        self.locators = settings.locators['pages']['wp_crawler']

    def crawl_website(self):
        self.click_on_element(locator=self.locators['crawl_button'])
