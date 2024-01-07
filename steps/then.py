from assertpy import assert_that
from pytest_bdd import then
from helpers.ssh_client import SSHClient
from helpers.utils import Settings as settings
from dsl.pages.wp_crawler import WPCrawlerPage
from helpers.utils import get_all_links
from loguru import logger


@then("Crawl results are displayed")
def check_results():
    WPCrawlerPage().wait_for_locator(settings.locators['pages']['wp_crawler']['crawl_results'])


@then('All hyperlinks present on homepage are in results')
def check_results_content():
    actual_links = get_all_links(settings.wordpress_creds['host'])
    links_from_crawl = WPCrawlerPage().get_crawl_results()
    logger.info(actual_links)
    logger.info(links_from_crawl)
    assert_that(len(actual_links)).is_equal_to(len(links_from_crawl)), "All hyperlinks on homepage were not displayed " \
                                                                       "in results"


@then('Sitemap file is deleted')
def check_for_sitemap_file():
    ssh_client = SSHClient(ssh_host=settings.ssh_creds['host'], port=settings.ssh_creds['port'],
                           username=settings.ssh_creds['username'],
                           password=settings.ssh_creds['password'])
    ssh_client.connect()
    command = 'find clickandbuilds/projectwordpress/ -type f -iname "*sitemap.html"'
    result = ssh_client.run_command(command)
    logger.info(result)
    ssh_client.close()
    assert_that(result).is_false(), "sitemap.html file was not deleted"
