from loguru import logger
from dsl.base_actions import BaseActions
from helpers.utils import Settings as settings, get_absolute_path


class WPPluginsPage(BaseActions):
    def __init__(self):
        super().__init__(settings.page)
        self.locators = settings.locators['pages']['plugins_page']

    def add_wp_crawler(self):
        self.click_on_element(text='Add New Plugin')
        self.click_on_element(button='Upload Plugin')
        path_to_plugin = get_absolute_path('wp-crawler-wpplugin.zip')
        self.file_chooser(path_to_file=path_to_plugin, locator=self.locators['choose_file_button'])
        self.click_on_element(button='Install Now')
        self.wait_for_locator(locator=self.locators['installation_confirmation'])
        logger.info("WP Crawler Successfully installed")

    def activate_plugin(self):
        self.click_on_element(text='Activate Plugin')
        self.wait_for_locator(locator=self.locators['activation_confirmation'])
        logger.info("WP Crawler Successfully Activated")

    def deactivate_plugin(self):
        self.click_on_element(locator=self.locators['deactivate_wp_crawler'])
        self.wait_for_locator(locator=self.locators['deactivation_confirmation'])
        logger.info("WP Crawler Successfully Deactivated")

    def delete_plugin(self):
        self.accept_dialog_promt()
        self.click_on_element(locator=self.locators['delete_wp_crawler'])
        self.wait_for_locator(locator=self.locators['deletion_confirmation'])
        logger.info("WP Crawler Successfully Deleted")
