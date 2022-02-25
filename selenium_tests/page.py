from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from .locators import IndexPageLocators
import time




class BasePage(object):


    def __init__(self, driver):
        self.driver = driver

    def do_clear(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_click(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_submit(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()

    def do_send_keys(self, locator, text):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_element_text(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def select_value(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()




    


class IndexPage(BasePage):

    def is_title_matches(self):
        return 'Famous Investors' in self.driver.title

    def is_index_heading_displayed_correctly(self):
        index_heading = self.get_element_text(IndexPageLocators.INDEX_HEADING)
        text = 'Famous Investors'
        return text in index_heading

    def is_arrow_scroll_working(self):
        self.do_click(IndexPageLocators.ARROW_SCROLL)
        return '#form-wrapper' in self.driver.current_url

    '''def is_investor_form_working(self):
        self.do_clear(IndexPageLocators.FULL_NAME)
        self.do_send_keys(IndexPageLocators.FULL_NAME, 'charlie munger')
        subs = self.get_elements(IndexPageLocators.SUBMIT)
        sub = subs[0]
        W(self.driver, 10).until(EC.element_to_be_clickable(sub)).click()
        time.sleep(10)'''











    

    