from django.core.urlresolvers import reverse, resolve


from test_plus.test import TestCase

class TestCustomersUrls(TestCase):
    """Test urls for customers app"""
    
    def setUp(self):
        self.user = self.make_user()
        
    
    def test_customers_list_reverse(self):
        """customers:index should reverse to /customers/."""
        self.assertEqual(reverse('customers:index'), '/customers/')
        
    def test_customers_list_resolve(self):
        """/customers/ should resolve to customers:index."""
        self.assertEqual(resolve('/customers/').view_name, 'customers:index')
        
    def test_customers_add_reverse(self):
        """customer:add should reverse to /customers/add"""
        self.assertEqual(reverse('customers:add'), '/customers/add/')
        
    def test_customers_add_resolve(self):
        """/customers/add should reverse to  customer:add"""
        self.assertEqual(resolve('/customers/add/').view_name, 'customers:add')
        
    def test_customers_update_reverse(self):
        """customer:update should reverse to /customers/update/"""
        self.assertEqual(reverse('customers:update', kwargs={'id' : 1}), '/customers/update/1/')
        
    def test_customers_update_resolve(self):
        """ /customers/update/ should reverse to customer:update"""
        self.assertEqual(resolve('/customers/update/1/').view_name, 'customers:update' )
        
    def test_customers_detail_reverse(self):
        """customer:detail should reverse to /customers/1"""
        self.assertEqual(reverse('customers:detail', kwargs={'id' : 1}), '/customers/detail/1/')
        
    def test_customers_detail_resolve(self):
        """/customers/1 should resolve to customer:detail """
        self.assertEqual(resolve('/customers/detail/1/').view_name, 'customers:detail')
        
    def test_customers_delete_reverse(self):
        """customer:delete should reverse to /customers/delete/"""
        self.assertEqual(reverse('customers:delete', kwargs={'id' : 1}), '/customers/delete/1/')
        
    def test_customers_delete_resolve(self):
        """/customers/delete/ should resolve to customer:delete"""
        self.assertEqual(resolve('/customers/delete/1/').view_name, 'customers:delete')
        
    ## Vendor testcases
    
    def test_vendors_list_reverse(self):
        """customers:vendors should reverse to /customers/vendors."""
        self.assertEqual(reverse('customers:vendors'), '/customers/vendors/')
        
    def test_vendors_list_resolve(self):
        """/customers/vendors should resolve to customers:vendors."""
        self.assertEqual(resolve('/customers/vendors/').view_name, 'customers:vendors')
        
    def test_vendors_add_reverse(self):
        """customer:addVendor should reverse to /customers/addVendor"""
        self.assertEqual(reverse('customers:addVendor'), '/customers/addVendor/')
        
    def test_vendors_add_resolve(self):
        """/customers/add should reverse to  customer:add"""
        self.assertEqual(resolve('/customers/addVendor/').view_name, 'customers:addVendor')
        
    def test_vendors_update_reverse(self):
        """customer:updateVendor should reverse to /customers/updateVendor/"""
        self.assertEqual(reverse('customers:updateVendor', kwargs={'id' : 1}), '/customers/updateVendor/1/')
        
    def test_vendors_update_resolve(self):
        """ /customers/updateVendor/ should reverse to customer:updateVendor"""
        self.assertEqual(resolve('/customers/updateVendor/1/').view_name, 'customers:updateVendor' )
        
    def test_vendors_detail_reverse(self):
        """customer:detailVendor should reverse to /customers/1"""
        self.assertEqual(reverse('customers:detailVendor', kwargs={'id' : 1}), '/customers/detailVendor/1/')
        
    def test_vendors_detail_resolve(self):
        """/customers/detailVendor/1 should resolve to customer:detailVendor """
        self.assertEqual(resolve('/customers/detailVendor/1/').view_name, 'customers:detailVendor')
        
    def test_vendors_delete_reverse(self):
        """customer:deleteVendor should reverse to /customers/deleteVendor/"""
        self.assertEqual(reverse('customers:deleteVendor', kwargs={'id' : 1}), '/customers/deleteVendor/1/')
        
    def test_vendors_delete_resolve(self):
        """/customers/deleteVendor/ should resolve to customer:deleteVendor"""
        self.assertEqual(resolve('/customers/deleteVendor/1/').view_name, 'customers:deleteVendor')