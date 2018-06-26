import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

BEHAVE_DEBUG_ON_ERROR = False

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
        time.sleep(1)
        try:
            context.browser.find_element_by_id(
                'signup_password'
            ).send_keys('gupiehaslo')
        except:
            context.browser.find_element_by_css_selector(
                '.magiclink_password_container'
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

def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import ipdb
        ipdb.post_mortem(step.exc_traceback)

def after_feature(context, feature):
    if "logout" in feature.tags:
        WebDriverWait(context.browser, 10).until(
            EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[id="account_button"]')
            )
        ).click()
        WebDriverWait(context.browser, 10).until(
            EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[id="logout_button"]')
            )
        ).click()
        WebDriverWait(context.browser, 10).until(
            EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[class="ui_button btn_1 chrome blue"]')
            )
        ).click()
        
def after_all(context):
    context.browser.quit()
