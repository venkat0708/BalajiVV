#python standard
from time import sleep

#third party packages
from selenium import webdriver
from test_plus import TestCase
from selenium.webdriver.common.keys import Keys


SLEEP_TIME = 5


class TestCustomersApp(TestCase):
    """To test functinality of all the customer pages"""

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        self.browser.maximize_window()
        self.browser.get('http://localhost:8000/accounts/login')
        #sleep(SLEEP_TIME)


        username = self.browser.find_element_by_id("id_login")
        password = self.browser.find_element_by_id("id_password")

        username.send_keys("kvreddy")
        password.send_keys("vesneven")
        login_attempt = self.browser.find_element_by_xpath("//*[@type='submit']")
        login_attempt.submit()
        #sleep(SLEEP_TIME)

    def tearDown(self):
        self.browser.quit()

    def test_events_pages(self):
        self.browser.get('http://localhost:8000/booking/events')
        sleep(30)
        assert 'Events' == self.browser.title
        assert 'list of Events' == self.browser.find_element_by_tag_name('h2').text
