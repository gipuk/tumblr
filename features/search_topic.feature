@login
@logout
Feature: As a logged user I want to find blog with my favorite topic

Scenario Outline: Find blog
When I enter "<topic>" in search bar
And I choose suggested "<topic>"
Then blogs to my favorite "<topic>" are shown

Examples:
| topic      |
|Harry Potter|
|John Porter |
|Will Smith  |


