from dsl.base_actions import BaseActions
from helpers.utils import Settings as settings, yaml_files, get_absolute_path, load_yaml


class WPLoginPage(BaseActions):
    def __init__(self):
        super().__init__(settings.page)
        self.locators = settings.locators['pages']['login_page']

    def login_to_dashboard(self, username, password):
        self.navigate_to_page(url=f'{settings.host}/wp-admin')
        self.send_text(self.locators['username'], username)
        self.send_text(self.locators['password'], password)
        self.click_on_element(locator=self.locators['login_button'])
        self.wait_for_locator(settings.locators['pages']['dashboard_page']['menu_item'].format(item_name='Dashboard'))

