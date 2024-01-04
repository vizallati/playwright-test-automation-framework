from pytest_bdd import when
from dsl.pages.wp_crawler import WPCrawlerPage
from dsl.pages.wp_dashboard import WPDashboardPage
from dsl.pages.wp_login import WPLoginPage
from dsl.pages.wp_plugins import WPPluginsPage


@when("I click on the crawl button in wp crawl admin page")
def trigger_crawl():
    WPDashboardPage().hover_over_menu_item(menu_item='Tools')
    WPDashboardPage().select_wp_crawler()
    WPCrawlerPage().crawl_website()
