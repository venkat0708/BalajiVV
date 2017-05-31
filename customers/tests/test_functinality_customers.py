'''
Created on 27-May-2017

@author: venkat
'''

#python standard
from time import sleep

#third party packages
from selenium import webdriver
from test_plus import TestCase
from selenium.webdriver.common.keys import Keys


#private packages
from.data_for_test import data, errors, SLEEP_TIME

def fill_form(inputs, form_data):
    inputs['name'].send_keys(form_data['name'])
    inputs['address'].send_keys(form_data['address'])
    inputs['city'].send_keys(form_data['city'])
    inputs['phone_number'].send_keys(form_data['phone_number'])
    inputs['submit'].submit()
    sleep(SLEEP_TIME*2)
    

class TestCustomersApp(TestCase):
    """To test functinality of all the customer pages"""
    
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
        self.browser.quit()
        
        
    def test_customers_pages(self):
        self.browser.get('http://localhost:8000/customers/')
        
        assert 'Customers' == self.browser.title
        assert 'list of customers' == self.browser.find_element_by_tag_name('h2').text
        table = self.browser.find_element_by_class_name('table')
        rows = table.find_elements_by_tag_name('tr')
        assert len(rows) == 4
        
        add_customer = self.browser.find_element_by_partial_link_text("Add Customer")
        add_customer.click()
        sleep(SLEEP_TIME)
        cancel_button = self.browser.find_element_by_class_name('btn-secondary')
        cancel_button.click()
        assert 'Customers' == self.browser.title
        assert 'list of customers' == self.browser.find_element_by_tag_name('h2').text
        table = self.browser.find_element_by_class_name('table')
        rows = table.find_elements_by_tag_name('tr')
        assert len(rows) == 4
        
        
        add_customer = self.browser.find_element_by_partial_link_text("Add Customer")
        add_customer.click()
        sleep(SLEEP_TIME)
        assert 'Add Customer' == self.browser.title
        assert 'Add Customer' == self.browser.find_element_by_tag_name('h2').text
        
        elements = {}
        elements['name'] = self.browser.find_element_by_id('id_name')
        elements['address'] = self.browser.find_element_by_id('id_address')
        elements['city'] = self.browser.find_element_by_id('id_city')
        elements['phone_number'] = self.browser.find_element_by_id('id_phone_number')
        elements['submit'] = self.browser.find_element_by_xpath("//*[@type='submit']")
        
        invalid_customer = {}
        invalid_customer['name'] = data['invalid_name']
        invalid_customer['address'] =data['address']
        invalid_customer['city'] =data['invalid_city']
        invalid_customer['phone_number'] =data['invalid_phone_number_length']
        
        fill_form(elements, invalid_customer)
        
        name_error = self.browser.find_element_by_id('error_1_id_name')
        city_error = self.browser.find_element_by_id('error_1_id_city')
        phone_number_error = self.browser.find_element_by_id('error_1_id_phone_number')
        
        assert errors['name_error'] == name_error.text
        assert errors['city_error'] == city_error.text
        assert errors['phone_number_error'] == phone_number_error.text
        
        self.browser.get(self.browser.current_url)
        
        elements = {}
        elements['name'] = self.browser.find_element_by_id('id_name')
        elements['address'] = self.browser.find_element_by_id('id_address')
        elements['city'] = self.browser.find_element_by_id('id_city')
        elements['phone_number'] = self.browser.find_element_by_id('id_phone_number')
        elements['submit'] = self.browser.find_element_by_xpath("//*[@type='submit']")
        
        invalid_customer = {}
        invalid_customer['name'] = data['valid_name']
        invalid_customer['address'] =data['address']
        invalid_customer['city'] =data['valid_city']
        invalid_customer['phone_number'] =data['invalid_phone_number_with_alphabets']
        
        fill_form(elements, invalid_customer)
        
        phone_number_error = self.browser.find_element_by_id('error_1_id_phone_number')
        assert errors['phone_number_error'] == phone_number_error.text
        
        self.browser.get(self.browser.current_url)
        
        elements = {}
        elements['name'] = self.browser.find_element_by_id('id_name')
        elements['address'] = self.browser.find_element_by_id('id_address')
        elements['city'] = self.browser.find_element_by_id('id_city')
        elements['phone_number'] = self.browser.find_element_by_id('id_phone_number')
        elements['submit'] = self.browser.find_element_by_xpath("//*[@type='submit']")
        
        valid_customer = {}
        valid_customer['name'] = data['valid_name']
        valid_customer['address'] =data['address']
        valid_customer['city'] =data['valid_city']
        valid_customer['phone_number'] =data['valid_phone_number']
        
        fill_form(elements, valid_customer)
        
        assert 'Customers' == self.browser.title
        assert 'list of customers' == self.browser.find_element_by_tag_name('h2').text
        table = self.browser.find_element_by_class_name('table')
        rows = table.find_elements_by_tag_name('tr')
        assert len(rows) == 5
        
        
        delete_row = self.browser.find_elements_by_tag_name('tr')[-1]
        button = delete_row.find_element_by_class_name('btn-danger')
        button.click()
        
        delete_button = self.browser.find_element_by_class_name('btn-danger')
        delete_button.click()
        
        assert 'Customers' == self.browser.title
        assert 'list of customers' == self.browser.find_element_by_tag_name('h2').text
        table = self.browser.find_element_by_class_name('table')
        rows = table.find_elements_by_tag_name('tr')
        assert len(rows) == 4
        
        
    def test_vendors_pages(self):
        self.browser.get('http://localhost:8000/customers/vendors')
        
        assert 'Vendors' == self.browser.title
        assert 'list of vendors' == self.browser.find_element_by_tag_name('h2').text
        table = self.browser.find_element_by_class_name('table')
        rows = table.find_elements_by_tag_name('tr')
        assert len(rows) == 4
        
        add_vendor = self.browser.find_element_by_partial_link_text("Add Vendor")
        add_vendor.click()
        sleep(SLEEP_TIME)
        cancel_button = self.browser.find_element_by_class_name('btn-secondary')
        cancel_button.click()
        assert 'Vendors' == self.browser.title
        assert 'list of vendors' == self.browser.find_element_by_tag_name('h2').text
        table = self.browser.find_element_by_class_name('table')
        rows = table.find_elements_by_tag_name('tr')
        assert len(rows) == 4
        
        
        add_vendor = self.browser.find_element_by_partial_link_text("Add Vendor")
        add_vendor.click()
        sleep(SLEEP_TIME)
        assert 'Add Vendor' == self.browser.title
        assert 'Add Vendor' == self.browser.find_element_by_tag_name('h2').text
        
        elements = {}
        elements['name'] = self.browser.find_element_by_id('id_name')
        elements['address'] = self.browser.find_element_by_id('id_address')
        elements['city'] = self.browser.find_element_by_id('id_city')
        elements['phone_number'] = self.browser.find_element_by_id('id_phone_number')
        elements['submit'] = self.browser.find_element_by_xpath("//*[@type='submit']")
        
        invalid_vendor = {}
        invalid_vendor['name'] = data['invalid_name']
        invalid_vendor['address'] =data['address']
        invalid_vendor['city'] =data['invalid_city']
        invalid_vendor['phone_number'] =data['invalid_phone_number_length']
        
        fill_form(elements, invalid_vendor)
        
        name_error = self.browser.find_element_by_id('error_1_id_name')
        city_error = self.browser.find_element_by_id('error_1_id_city')
        phone_number_error = self.browser.find_element_by_id('error_1_id_phone_number')
        
        assert errors['name_error'] == name_error.text
        assert errors['city_error'] == city_error.text
        assert errors['phone_number_error'] == phone_number_error.text
        
        self.browser.get(self.browser.current_url)
        
        elements = {}
        elements['name'] = self.browser.find_element_by_id('id_name')
        elements['address'] = self.browser.find_element_by_id('id_address')
        elements['city'] = self.browser.find_element_by_id('id_city')
        elements['phone_number'] = self.browser.find_element_by_id('id_phone_number')
        elements['submit'] = self.browser.find_element_by_xpath("//*[@type='submit']")
        
        invalid_vendor = {}
        invalid_vendor['name'] = data['valid_name']
        invalid_vendor['address'] =data['address']
        invalid_vendor['city'] =data['valid_city']
        invalid_vendor['phone_number'] =data['invalid_phone_number_with_alphabets']
        
        fill_form(elements, invalid_vendor)
        
        phone_number_error = self.browser.find_element_by_id('error_1_id_phone_number')
        assert errors['phone_number_error'] == phone_number_error.text
        
        self.browser.get(self.browser.current_url)
        
        elements = {}
        elements['name'] = self.browser.find_element_by_id('id_name')
        elements['address'] = self.browser.find_element_by_id('id_address')
        elements['city'] = self.browser.find_element_by_id('id_city')
        elements['phone_number'] = self.browser.find_element_by_id('id_phone_number')
        elements['submit'] = self.browser.find_element_by_xpath("//*[@type='submit']")
        
        valid_vendor = {}
        valid_vendor['name'] = data['valid_name']
        valid_vendor['address'] =data['address']
        valid_vendor['city'] =data['valid_city']
        valid_vendor['phone_number'] =data['valid_phone_number']
        
        fill_form(elements, valid_vendor)
        
        assert 'Vendors' == self.browser.title
        assert 'list of vendors' == self.browser.find_element_by_tag_name('h2').text
        table = self.browser.find_element_by_class_name('table')
        rows = table.find_elements_by_tag_name('tr')
        assert len(rows) == 5
        
        
        delete_row = self.browser.find_elements_by_tag_name('tr')[-1]
        button = delete_row.find_element_by_class_name('btn-danger')
        button.click()
        
        delete_button = self.browser.find_element_by_class_name('btn-danger')
        delete_button.click()
        
        assert 'Vendors' == self.browser.title
        assert 'list of vendors' == self.browser.find_element_by_tag_name('h2').text
        table = self.browser.find_element_by_class_name('table')
        rows = table.find_elements_by_tag_name('tr')
        assert len(rows) == 4
        
        
        