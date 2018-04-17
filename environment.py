from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()

def before_feature(context, feature):
    if "login" in feature.tags:
        context.browser.get('https://www.tumblr.com/')
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
        WebDriverWait(context.browser, 10).until(
            EC.visibility_of_element_located(
            (By.ID, 'signup_password')
            )
        ).send_keys('gupiehaslo')
        WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[class="signup_login_btn active"]')
            )
        ).click()

def after_all(context):
    context.browser.quit()
