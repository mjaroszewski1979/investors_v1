from selenium.webdriver.common.by import By

class IndexPageLocators(object):
    
    INDEX_HEADING = (By.XPATH, "//section//header//h1")
    ARROW_SCROLL = (By.CLASS_NAME, 'scrolly')
    FULL_NAME = (By.ID, 'full_name')
    SUBMIT = (By.CSS_SELECTOR, "input[type='submit'] and value='Submit']")


