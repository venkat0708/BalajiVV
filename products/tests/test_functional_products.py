from selenium import webdriver
from test_plus import TestCase





class Test_Category_pages(TestCase):
    """To test all the pages related to category management"""
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.close()
        
    def test_index_page(self):
        self.browser.get('http://localhost:8000/products/categories/')
        assert 'categories' == self.browser.title