@login
@logout
Feature: As a logged user I want follow user

Scenario: Follow  user
When I enter user in search field
And I click Follow button
Then User is available on Following Tumblrs list
