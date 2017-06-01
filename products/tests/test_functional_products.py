from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_plus import TestCase
from time import sleep


SLEEP_TIME = 1

class TestCategoryApp(TestCase):
    """To test all the pages related to category management"""
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        self.browser.maximize_window()
        self.browser.get('http://localhost:8000/accounts/login')
        sleep(SLEEP_TIME)
        
        
        username = self.browser.find_element_by_id("id_login")
        password = self.browser.find_element_by_id("id_password")

        username.send_keys("kvreddy")
        password.send_keys("vesneven")
        login_attempt = self.browser.find_element_by_xpath("//*[@type='submit']")
        login_attempt.submit()
        sleep(SLEEP_TIME)
        
    def tearDown(self):
        self.browser.close()
        
    def test_index_page(self):
        self.browser.get('http://localhost:8000/products/categories/')
        assert 'Categories' == self.browser.title