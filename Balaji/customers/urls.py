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
        regex=r'^update/(?P<id>[0-9]+)/$',
        view=views.Update_Customer,
        name='update'
    ),
    url(
        regex=r'^detail/(?P<id>[0-9]+)/$',
        view=views.Detail_Customer,
        name='detail'
    ),

    url(
        regex=r'^delete/(?P<id>[0-9]+)/$',
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
        regex=r'^updateVendor/(?P<id>[0-9]+)/$',
        view=views.Update_Vendor,
        name='updateVendor'
    ),

    url(
        regex=r'^detailVendor/(?P<id>[0-9]+)/$',
        view=views.Detail_Vendor,
        name='detailVendor'
    ),

     url(
        regex=r'^deleteVendor/(?P<id>[0-9]+)/$',
        view=views.Delete_Vendor,
        name='deleteVendor'
    ),


     url(
         regex=r'^staff/$',
         view=views.StaffIndexView.as_view(),
         name='Staff_Index'
     ),

     url(
       regex=r'^staff/(?P<pk>[\d]+)/$',
       view = views.StaffDetailView.as_view(),
       name = 'Staff_Detail'
     ),

     url(
       regex=r'^staff/add/$',
       view = views.StaffCreateView.as_view(),
       name = 'Staff_Create'
     ),

     url(
       regex=r'^staff/update/(?P<pk>[\d]+)/$',
       view = views.StaffUpdateView.as_view(),
       name = 'Staff_Update'
     ),

     url(
       regex=r'^staff/delete/(?P<pk>[\d]+)/$',
       view = views.StaffDeleteView.as_view(),
       name = 'Staff_Delete'
     ),
]
