from selenium import webdriver
from test_plus.test import TestCase
from selenium.webdriver.common.keys import Keys

from .data_for_test import  visitor_urls, login_user_urls, admin_urls

from time import sleep

class NewVisitorTest(TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
        
    def test_can_visit_home_page(self):
        self.browser.get('http://localhost:8000/')
        
        assert 'Balaji' in self.browser.title
        
        
        links = []
        urls = []
        
        for link in self.browser.find_elements_by_css_selector(".nav-link"):
            links.append(link)
            urls.append((link.get_attribute("href")))
            assert link.text in visitor_urls
        assert len(links) == len(visitor_urls)
        
        for u in urls:
            self.browser.get(u)
            self.browser.back()
            
             
        
        
    def test_can_visit_signup_page(self):
        self.browser.get('http://localhost:8000/accounts/signup')
        
        assert 'Signup' in self.browser.title
        
        
        links = []
        urls = []
        
        for link in self.browser.find_elements_by_css_selector(".nav-link"):
            links.append(link)
            urls.append((link.get_attribute("href")))
            assert link.text in visitor_urls
        assert len(links) == len(visitor_urls)
        
        for u in urls:
            self.browser.get(u)
            self.browser.back()
        
        
    def test_can_visit_signin_page(self):
        self.browser.get('http://localhost:8000/accounts/login')
        
        assert 'Sign In' in self.browser.title
        
        
        links = []
        urls = []
        
        for link in self.browser.find_elements_by_css_selector(".nav-link"):
            links.append(link)
            urls.append((link.get_attribute("href")))
            assert link.text in visitor_urls
        assert len(links) == len(visitor_urls)
        
        for u in urls:
            self.browser.get(u)
            self.browser.back()
        
        
        
    def test_can_signin_user(self):
        self.browser.get('http://localhost:8000/accounts/login')
        sleep(3)
        
        
        username = self.browser.find_element_by_id("id_login")
        password = self.browser.find_element_by_id("id_password")

        username.send_keys("venkat")
        password.send_keys("vesneven")
        login_attempt = self.browser.find_element_by_xpath("//*[@type='submit']")
        login_attempt.submit()
        sleep(3)
        
        assert 'http://localhost:8000/users/venkat/' == self.browser.current_url
        
        links = []
        urls = []
        
        for link in self.browser.find_elements_by_css_selector(".nav-link"):
            links.append(link)
            urls.append((link.get_attribute("href")))
            assert link.text in login_user_urls
        assert len(links) == len(login_user_urls)
        
        for u in urls:
            self.browser.get(u)
            self.browser.back()
            
        self.browser.get('http://localhost:8000/accounts/logout')
        
        signout = self.browser.find_element_by_xpath("//*[@type='submit']")
        signout.submit()
        sleep(1)
        assert 'Balaji' in self.browser.title
        
    def test_can_signin_admin(self):
        self.browser.get('http://localhost:8000/accounts/login')
        sleep(3)
        
        
        username = self.browser.find_element_by_id("id_login")
        password = self.browser.find_element_by_id("id_password")

        username.send_keys("kvreddy")
        password.send_keys("vesneven")
        login_attempt = self.browser.find_element_by_xpath("//*[@type='submit']")
        login_attempt.submit()
        sleep(3)
        
        assert 'http://localhost:8000/users/kvreddy/' == self.browser.current_url
        
        links = []
        urls = []
        
        for link in self.browser.find_elements_by_css_selector(".nav-link"):
            links.append(link)
            urls.append((link.get_attribute("href")))
            assert link.text in admin_urls
        assert len(links) == len(admin_urls)
        
        for u in urls:
            self.browser.get(u)
            self.browser.back()
            
        self.browser.get('http://localhost:8000/accounts/logout')
        
        signout = self.browser.find_element_by_xpath("//*[@type='submit']")
        signout.submit()
        sleep(1)
        assert 'Balaji' in self.browser.title
        
        