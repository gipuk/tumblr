Feature: As a logged user I want to find blog with my favorite topic

@new_browser
Scenario Outline: Find blog
Given user is logged
When I enter "<topic>" in search bar
And I choose suggested "<topic>"
Then blogs to my favorite "<topic>" are shown

Examples:
| topic      |
|Harry Potter|
| dog        |
| cat        |


