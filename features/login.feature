Feature: As a registered user I wan't to login to my account

@login
Scenario: Sucessful login
Given page is loaded
When I enter user login
And I enter password
When I click Log in button
Then I'm logged in
