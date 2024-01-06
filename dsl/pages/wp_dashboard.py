from dsl.base_actions import BaseActions
from helpers.utils import Settings as settings


class WPDashboardPage(BaseActions):
    def __init__(self):
        super().__init__(settings.page)
        self.locators = settings.locators['pages']['dashboard_page']

    def select_menu_item(self, menu_item):
        self.click_on_element(locator=self.locators['menu_item'].format(item_name=menu_item))

    def hover_over_menu_item(self, menu_item):
        self.hover_over_element(locator=self.locators['menu_item'].format(item_name=menu_item))

    def select_wp_crawler(self):
        self.click_on_element(locator=self.locators['wp_crawler'])
