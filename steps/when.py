from pytest_bdd import when
from dsl.pages.wp_crawler import WPCrawlerPage
from dsl.pages.wp_dashboard import WPDashboardPage


@when("I click on the crawl button in wp crawl admin page")
def trigger_crawl():
    wp_dashboard = WPDashboardPage()
    wp_dashboard.hover_over_menu_item(menu_item='Tools')
    wp_dashboard.select_wp_crawler()
    WPCrawlerPage().crawl_website()
