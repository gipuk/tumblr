import os
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


@when('I enter "{topic}" in search bar')
def step_impl(context, topic):
    context.browser.find_element_by_css_selector('[id="search_query"]').clear()
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[id="search_query"]')
        )
    ).send_keys(topic)


@when('I choose suggested "{topic}"')
def step_impl(context, topic):
    link = topic.replace(" ","+")
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


@when('I click add file from dashboard')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[class="icon_post_photo"]')
        )
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.dropzone-add-photo-icon')
        )
    )
    element = context.browser.find_element(
        By.CSS_SELECTOR,
        '.dropzone-add-photo-icon'
    )
    context.browser.execute_script("arguments[0].click();", element)


@when('I choose file')
def step_impl(context):
    imagepath = os.path.abspath('testbug.png')
    context.browser.find_element(
        By.CSS_SELECTOR,
        'input[name="photo"]'
    ).send_keys(imagepath) 
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[class="button-area create_post_button"]')
        )
    ).click()
    time.sleep(5)


@then('File is added to my blog')
def step_impl(context):
    context.browser.refresh()
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[id="account_button"]')
        )
    )
    element = context.browser.find_element(
        By.CSS_SELECTOR,
        '[id="account_button"]'
    )
    context.browser.execute_script("arguments[0].click();", element)
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[class="blog-sub-nav-item-link"]')
        )
    )
    
    context.browser.find_element_by_css_selector(
        '[href="/blog/qrak"].blog-sub-nav-item-link'
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[title="Post Options"]')
        )
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[title="Delete"]')
        )
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[class="ui_button btn_1 chrome blue"]')
        )
    ).click()


@when('There is a post in dashboard')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[id="account_button"]')
        )
    )
    element = context.browser.find_element(
        By.CSS_SELECTOR,
        '[id="account_button"]'
    )
    context.browser.execute_script("arguments[0].click();", element)
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[class="blog-sub-nav-item-link"]')
        )
    ).click()


@when('I click delete button')
def step_impl(context):
    post_count = len(context.browser.find_elements_by_css_selector(
        '[class="post_header"]'
        )
    )
    for x in range (0, post_count):
        WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[title="Post Options"]')
            )
        ).click()
        WebDriverWait(context.browser, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[title="Delete"]')
            )
        ).click()
        WebDriverWait(context.browser, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[class="ui_button btn_1 chrome blue"]')
            )
        ).click()
        time.sleep(2)


@then('Posts are deleted from my dashboard')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, '[title="Post Options"]')
        )
    )


@when('I enter user in search field')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[id="account_button"]')
        )
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[href="/following"]')
        )
    ).click()


@when('I click Follow button')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[name="follow_this"]')
        )
    ).send_keys("123")
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,'[name="submit"]')
        )
    ).click()


@then('User is available on Following Tumblrs list')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[id="unfollow_button_123"]')
        )
    )


@given('User 123 is followed')
def step_impl(context):
    context.execute_steps('''
        when I enter user in search field
        and I click Follow button
        then User is available on Following Tumblrs list
        ''')


@when('I find user')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[id="account_button"]')
        )
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[href="/following"]')
        )
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[id="unfollow_button_123"]')
        )
    ).click()


@when('I click Unfollow button')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[class="ui_button btn_1 chrome blue"]')
        )
    )
    element = context.browser.find_element(
        By.CSS_SELECTOR,
        '[class="ui_button btn_1 chrome blue"]'
    )
    context.browser.execute_script("arguments[0].click();", element)


@then('User is deleted from Followin Tumblrs list')
def step_impl(context):
    context.browser.refresh()
    import ipdb; ipdb.set_trace()
    assert len(context.browser.find_elements_by_css_selector(
        '[id="unfollow_button_123"]'
        )
    ) is None
