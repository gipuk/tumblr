import time
from behave import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@when('I click Account')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[id="account_button"]')
        )
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[href="/settings"]')
        )
    ).click()

@when('I change "{lang}" and "{LA}"')
def step_impl(context, lang, LA):
    select = Select(context.browser.find_element_by_id("user_language"))
    select.select_by_value("{}".format(LA))

@then('page is availble in "{word}"')
def step_impl(context, word):
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//div/h3[text() = "{}"]'.format(word))
        )
    )
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[id="account_button"]')
        )
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[href="/logout"]')
        )
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[class="ui_button btn_1 chrome blue"]')
        )
    ).click()

@when('I enter "{topic}" in search bar')
def step_impl(context, topic):
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[id="search_query"]')
        )
    ).send_keys(topic)

@when('I choose suggested "{topic}"')
def step_impl(context, topic):
    link = topic.replace(" ","+")
    print(link)
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 
            '[href="https://www.tumblr.com/search/{}"]'.format(link)
        ))
    ).click()

@then('blogs to my favorite "{topic}" are shown')
def step_impl(context, topic):
    capital = topic.lower()
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//div/h1[text()="{}"]'.format(capital))
        )
    )
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[id="account_button"]')
        )
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[href="/logout"]')
        )
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[class="ui_button btn_1 chrome blue"]')
        )
    ).click()
