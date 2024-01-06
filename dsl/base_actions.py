import re
from playwright.sync_api import Page


class BaseActions:
    def __init__(self, page: Page):
        """
        Base class containing common methods for interacting with web pages using Playwright.
        This class is intended to be inherited by various page object models,
        providing a set of reusable methods for navigation, element interaction...

        Args:
            page (Page): The Playwright Page instance.
        """
        self.page = page

    def navigate_to_page(self, url):
        """
        Navigate to the specified URL.

        Args:
            url (str): The URL to navigate to.
        """
        self.page.goto(url, timeout=50000)

    def click_on_element(self, **kwargs):
        """
        Click on an element based on the provided parameters.

        Args:
            **kwargs: Keyword arguments to specify the element to click.
                - button (str): Button text.
                - locator (str): Element locator.
                - text (str): Element text.

        Raises:
            ValueError: If an invalid element is provided.
        """
        if kwargs.get('button'):
            self.page.get_by_role("button", name=re.compile(kwargs['button'], re.IGNORECASE)).last.click()
        elif kwargs.get('locator'):
            self.page.locator(kwargs['locator']).click()
        elif kwargs.get('text'):
            self.page.get_by_text(kwargs['text']).click()
        else:
            raise ValueError('Invalid element')

    def send_text(self, locator, text):
        """
        Clear the input field and send the specified text.

        Args:
            locator (str): Element locator.
            text (str): Text to send to the element.
        """
        self.page.locator(locator).clear()
        self.page.fill(locator, text)

    def get_text(self, locator):
        """
        Get the text content of an element.

        Args:
            locator (str): Element locator.

        Returns:
            str: The text content of the element.
        """
        return self.page.text_content(locator).strip()

    def previous_page(self):
        """
        Navigate to the previous page in the browser history.
        """
        self.page.go_back()

    def wait_for_locator(self, locator):
        """
        Wait for the specified element to appear on the page.

        Args:
            locator (str): Element locator.
        """
        self.page.wait_for_selector(locator, timeout=12000)

    def file_chooser(self, path_to_file, locator):
        """
        Open a file chooser dialog, select a file, and close the dialog.

        Args:
            path_to_file (str): Path to the file to be selected.
            locator (str): Element locator.
        """
        with self.page.expect_file_chooser() as fc_info:
            self.click_on_element(locator=locator)
        file_chooser = fc_info.value
        file_chooser.set_files(path_to_file)

    def select_option(self, locator, option):
        """
        Select the specified option from a dropdown.

        Args:
            locator (str): Element locator.
            option (str): Option text.
        """
        self.page.locator(locator).select_option(option)

    def hover_over_element(self, locator):
        """
        Hover over the specified element.

        Args:
            locator (str): Element locator.
        """
        self.page.hover(selector=locator)

    def handle_dialog(self, dialog):
        """
        Handle a dialog by accepting it.

        Args:
            dialog: The dialog instance.
        """
        dialog.accept()

    def accept_dialog_promt(self):
        """
        Accept a dialog prompt once it appears on the page.
        """
        self.page.once("dialog", self.handle_dialog)

    def wait_for_page_load(self):
        self.page.wait_for_load_state('load')
