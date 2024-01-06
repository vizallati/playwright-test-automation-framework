Feature: Crawl Trigger and Results Display
  As an administrator, I want to see how my website web pages are linked to my home page
  so that I can manually search for ways to improve my SEO rankings.

Background:
  Given I have the wp crawl plugin installed and activated


  Scenario: Trigger crawl
    When I navigate to the crawl admin page and click on crawl button
    Then Crawl results are displayed

  Scenario: Check crawl results
    When I navigate to the crawl admin page and click on crawl button
    Then Crawl results are displayed
    And All hyperlinks present on homepage are in results

  Scenario: Deletion of previous crawl results
    When I navigate to the crawl admin page and click on crawl button
    And I click on the crawl button for the second time
    Then All hyperlinks present on homepage are in results

  Scenario: Check deletion of sitemap file after crawl
    Given Sitemap file exists on server
    When I navigate to the crawl admin page and click on crawl button
    Then Crawl results are displayed
    And Sitemap file is deleted
