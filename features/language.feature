@login
@logout

Feature: As logged user I wan to change language

Scenario Outline: Change language
    When I click Account
    And I change "<lang>" and "<LA>"
    Then page is availble in "<word>"

    Examples:
    | lang             | LA    |word      |
    | English          | en_US | Language |
    | Deutsch          | de_DE | Sprache  |
    | Français         | fr_FR | Langue   |
    | Italiano         | it_IT | Lingua   |
    | 日本語            |ja_JP  | 言語      |
    | Türkçe           | tr_TR | Dil      |
    | Español          | es_ES | Idioma   |
    | Pусский          | ru_RU | Язык     |
    | Polski           | pl_PL | Język    |
    | Português (PT)   | pt_PT | Idioma   |
    | Português (BR)   | pt_BR | Idioma   |
    | Nederlands       | nl_NL | Taal     |
    | 한국어             | ko_KR | 언어     |
    | 简体中文           | zh_CN | 语言     |
    | 繁體中文 (台灣)     | zh_TW | 語言     |
    | 繁體中文 (香港)     | zh_HK | 語言     |
    | Bahasa Indonesia | id_ID | Bahasa   |
    | हिंदी           | hi_IN | भाषा    |
