import time
from pytest_bdd import when
from dsl.pages.wp_crawler import WPCrawlerPage
from dsl.pages.wp_dashboard import WPDashboardPage


@when("I navigate to the crawl admin page and click on crawl button")
def navigate_and_trigger_crawl():
    wp_dashboard = WPDashboardPage()
    wp_dashboard.hover_over_menu_item(menu_item='Tools')
    wp_dashboard.select_wp_crawler()
    WPCrawlerPage().crawl_website()


@when("I click on the crawl button for the second time")
def trigger_crawl():
    time.sleep(15)
    WPCrawlerPage().crawl_website()
