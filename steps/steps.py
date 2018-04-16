from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from behave import *
import time

@given('page is loaded')
def step_impl(context):
    context.browser.get('https://www.tumblr.com/')

@when('I enter user login')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.ID, 'signup_login_button')
        )
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.ID, 'signup_determine_email')
        )
    ).send_keys('yaqbeush@gmail.com')
    context.browser.find_element_by_id(
        'signup_forms_submit'
        ).click()

@when('I enter password')
def step_impl(context):
     WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.ID, 'signup_password')
        )
    ).send_keys('gupiehaslo')

@when('I click Log in button')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[class="signup_login_btn active"]')
        )
    ).click()

@then("I'm logged in")
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[id="user_tools"]')
        )
    )

@given('user is logged')
def step_impl(context):
    context.execute_steps('''
    Given page is loaded
    When I enter user login
    And I enter password
    When I click Log in button
    Then I'm logged in
    ''')

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
