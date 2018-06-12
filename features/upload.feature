@loging
@logout
Feature: As logged user I want to add file to my blog

Scenario: Adding file from dashboard
    When I click add file from dashboard
    And I choose file
    Then File is added to my blog