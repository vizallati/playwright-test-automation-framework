from pytest_bdd import given


@given('I have the wp crawl plugin installed and activated')
def install_and_activate_wp_crawl(plugin_setup_and_teardown):
    pass


@given('Sitemap file exists on server')
def create_sitemap(create_sitemap_file):
    pass
