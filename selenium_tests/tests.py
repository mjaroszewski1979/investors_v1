from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from . import page
from api.models import Investor
from django.urls import reverse





class InvestorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome('selenium_tests/chromedriver.exe')
        self.driver.set_window_size(1920, 1080)
        
        self.new_investor = Investor.objects.create(
            full_name = 'george soros'
        )
        self.new_investor.save()

    def tearDown(self):
        self.new_investor.delete()
        self.driver.close()


    def test_indexpage(self):
        self.driver.get(self.live_server_url)
        index_page = page.IndexPage(self.driver)
        assert index_page.is_title_matches()
        assert index_page.is_index_heading_displayed_correctly()
        assert index_page.is_arrow_scroll_working()
        index_page.is_investor_form_working()








