from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.Index,
        name='index'
    ),

    url(
    	regex=r'^add/$',
    	view =views.Add_Customer,
    	name='add'
    ),
    url(
        regex=r'^update/(?P<id>[1-9]+)/$',
        view=views.Update_Customer,
        name='update'
    ),
    url(
        regex=r'^(?P<id>[1-9]+)/$',
        view=views.Detail_Customer,
        name='detail'
    ),
    
    url(
        regex=r'^delete/(?P<id>[1-9]+)/$',
        view=views.Delete_Customer,
        name='delete'
    ),
               
    url(
        regex=r'^vendors/$',
        view=views.Vendor_Index,
        name='vendors'
    ),
               
    url(
        regex=r'^addVendor/$',
        view =views.Add_Vendor,
        name='addVendor'
    ),
               
    url(
        regex=r'^updateVendor/(?P<id>[1-9]+)/$',
        view=views.Update_Vendor,
        name='updateVendor'
    ),
               
    url(
        regex=r'^detailVendor/(?P<id>[1-9]+)/$',
        view=views.Detail_Vendor,
        name='detailVendor'
    ),
               
     url(
        regex=r'^deleteVendor/(?P<id>[1-9]+)/$',
        view=views.Delete_Vendor,
        name='deleteVendor'
    ),
]
