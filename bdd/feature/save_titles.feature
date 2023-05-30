Feature: To extract titles from online and save it in a text document

  Scenario: Search for ProQuest on web and capture all the titles in the first page from google
    Given user launches the Google search page
    When he enters "ProQuest" and hits enter
    And he captures all titles from the webpage
    Then the user saves the titles in a text file
