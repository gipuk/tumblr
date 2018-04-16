from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()


#def before_scenario(context, scenario):
 #   if "new_browser" in scenario.tags:
 #       context.browser = webdriver.Chrome()



def after_scenario(context, scenario):
    if "close_browser" in scenario.tags:
        context.browser.close()
        #context.browser.execute_script('window.localStorage.clear();')
        #context.browser.refresh()


def after_all(context):
    context.browser.quit()
