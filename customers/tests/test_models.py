from test_plus.test import TestCase


from ..models import (Customer, Vendor)
from __builtin__ import isinstance

class CustomerTest(TestCase):
    def setUp(self):
        self.name = "testcustomer"
        self.address = "Test"
        self.city = "Test"
        self.phone_number = "9999999999"
        
        self.test_customer = Customer.objects.create(
                name = self.name,
                address = self.address,
                city = self.city,
                phone_number = self.phone_number,
            )
        
    def test_create_customer(self):
        assert isinstance(self.test_customer, Customer)
        
    def test_customers_count(self):
        assert Customer.objects.count() == 1
        
    def test_customers_data(self):
        customer = Customer.objects.get(name = 'testcustomer')
        assert customer.name == 'testcustomer'
        assert customer.__str__() == 'testcustomer'
        
    
class VendorTest(TestCase):
    def setUp(self):
        self.name = "testVendor"
        self.address = "Test"
        self.city = "Test"
        self.phone_number = "9999999999"
        
        self.test_vendor = Vendor.objects.create(
                name = self.name,
                address = self.address,
                city = self.city,
                phone_number = self.phone_number,
            )
        
    def test_create_vendor(self):
        assert isinstance(self.test_vendor, Vendor)
        
    def test_vendors_count(self):
        assert Vendor.objects.count() == 1
        
    def test_vendors_data(self):
        vendor = Vendor.objects.get(name = 'testVendor')
        assert vendor.name == 'testVendor'
        assert vendor.__str__ ()== 'testVendor'
        
        