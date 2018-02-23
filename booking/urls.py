from django.conf.urls import url

from .views import *
from . import views


urlpatterns = [
    url(
        regex=r'^events/$',
        view=EventIndexView.as_view(),
        name='Event_Index'
    ),

    url(
      regex=r'^event/(?P<pk>[\d]+)/$',
      view = EventDetailView.as_view(),
      name = 'Event_Detail'
    ),

    url(
      regex=r'^event/add/$',
      view = EventCreateView.as_view(),
      name = 'Event_Create'
    ),

    url(
      regex=r'^event/update/(?P<pk>[\d]+)/$',
      view = EventUpdateView.as_view(),
      name = 'Event_Update'
    ),

    url(
      regex=r'^event/delete/(?P<pk>[\d]+)/$',
      view = EventDeleteView.as_view(),
      name = 'Event_Delete'
    ),

    url(
        regex=r'^booked_services$',
        view=views.Booked_Service_Index,
        name='Booked_Service_Index'
    ),

    url(
    	regex=r'^booking/add/$',
    	view =views.Booked_Service_Add,
    	name='Booked_Service_Add'
    ),
    url(
        regex=r'^booking/update/(?P<id>[0-9]+)/$',
        view=views.Booked_Service_Update,
        name='Booked_Service_Update'
    ),
    url(
        regex=r'^booking/detail/(?P<id>[0-9]+)/$',
        view=views.Booked_Service_Detail,
        name='Booked_Service_Detail'
    ),

    url(
        regex=r'^booking/delete/(?P<id>[0-9]+)/$',
        view=views.Booked_Service_Delete,
        name='Booked_Service_Delete'
    ),

    ]
