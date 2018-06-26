@login
@logout
Feature: As a logged user I want usfollow user

Scenario: Unfollow  user
Given User 123 is followed
When I find user
And I click Unfollow button
Then User is deleted from Followin Tumblrs list
