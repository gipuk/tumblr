@login
@logout
Feature: As a logged user I wan't to delete all files from my blog

Scenario: Deleting all files from dashboard
When There is a post in dashboard
And I click delete button
Then Posts are deleted from my dashboard
