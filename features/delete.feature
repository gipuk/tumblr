@login
Feature: As a logged user I wan't to delete all files from my blog

Scenario: Deleting all files from dashboard
When There is a file in dashboard
And I choose file
And I click delete button
Then File is deleted from my dashboard