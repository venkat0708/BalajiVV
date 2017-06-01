from django.conf.urls import url

from .views import *


urlpatterns = [
    url(
        regex=r'^categories/$',
        view=CategoryIndexView.as_view(),
        name='Category_Index'
    ),
               
    url(
      regex=r'^category/(?P<pk>[\d]+)/$',
      view = CategoryDetailView.as_view(),
      name = 'Category_Detail'  
    ),
               
    url(
      regex=r'^category/add/$',
      view = CategoryCreateView.as_view(),
      name = 'Category_Create'  
    ),
               
    url(
      regex=r'^category/update/(?P<pk>[\d]+)/$',
      view = CategoryUpdateView.as_view(),
      name = 'Category_Update'  
    ),
               
    url(
      regex=r'^category/delete/(?P<pk>[\d]+)/$',
      view = CategoryDeleteView.as_view(),
      name = 'Category_Delete'  
    ),
               
]
