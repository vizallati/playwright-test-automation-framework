from pytest_bdd import then
from helpers.utils import Settings as settings
from dsl.pages.wp_crawler import WPCrawlerPage
from helpers.utils import get_all_links


@then("Crawl results are displayed")
def check_results():
    WPCrawlerPage().wait_for_locator(settings.locators['pages']['wp_crawler']['crawl_results'])


@then('All hyperlinks present on homepage are in results')
def check_results_content():
    actual_links = get_all_links("https://adjaniokpuegbe.com/")
    links_from_crawl = WPCrawlerPage().get_crawl_results()
    assert len(actual_links) == len(links_from_crawl)
    print('Legend')
