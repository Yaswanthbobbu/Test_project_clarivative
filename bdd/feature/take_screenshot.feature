Feature: To take screenshot for search results

  Scenario: Take the screenshot of the search results for QA
    Given user opens "ProQuest" website
    When user searches for "QA" in the top navigation
    Then user captures the screenshot of the search page