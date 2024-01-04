from dsl.base_actions import BaseActions
from helpers.utils import Settings as settings, yaml_files, get_absolute_path, load_yaml


class WPCrawlerPage(BaseActions):
    def __init__(self):
        super().__init__(settings.page)
        self.locators = settings.locators['pages']['wp_crawler']

    def crawl_website(self):
        self.click_on_element(locator=self.locators['crawl_button'])

    def get_crawl_results(self):
        list_items = self.page.query_selector_all(self.locators['crawl_results'])
        all_results = []
        # Iterate through the result items and append results
        for list_item in list_items:
            text_content = list_item.text_content()
            all_results.append(text_content)
        return all_results
