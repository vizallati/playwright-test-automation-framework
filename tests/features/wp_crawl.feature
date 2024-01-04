Feature: Homepage Crawling
  As an administrator, I want to see how my website web pages are linked to my home page
  so that I can manually search for ways to improve my SEO rankings.

Background:
  Given I have the wp crawl plugin installed and activated


  Scenario: Trigger crawl
    When I click on the crawl button in wp crawl admin page
    Then Crawl results are displayed

  Scenario: Check crawl results
    When I click on the crawl button in wp crawl admin page
    Then Crawl results are displayed
    And All hyperlinks present on homepage are in results