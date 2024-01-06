import pytest
from pytest_bdd import scenario
from steps.given import *
from steps.when import *
from steps.then import *


@pytest.mark.case_id('WP-001')
@scenario('features/wp_crawl.feature', 'Trigger crawl')
def test_trigger_crawl():
    pass


@pytest.mark.case_id('WP-002')
@scenario('features/wp_crawl.feature', 'Check crawl results')
def test_check_crawl_results():
    pass


@pytest.mark.case_id('WP-003')
@scenario('features/wp_crawl.feature', 'Deletion of previous crawl results')
def test_check_crawl_results_deletion():
    pass


@pytest.mark.case_id('WP-004')
@scenario('features/wp_crawl.feature', 'Check deletion of sitemap file after crawl')
def test_check_sitemap_deletion():
    pass
