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
    
    url(
        regex=r'^products/$',
        view=ProductIndexView.as_view(),
        name='Product_Index'
    ),
               
    url(
      regex=r'^product/(?P<pk>[\d]+)/$',
      view = ProductDetailView.as_view(),
      name = 'Product_Detail'  
    ),
               
    url(
      regex=r'^product/add/$',
      view = ProductCreateView.as_view(),
      name = 'Product_Create'  
    ),
               
    url(
      regex=r'^product/update/(?P<pk>[\d]+)/$',
      view = ProductUpdateView.as_view(),
      name = 'Product_Update'  
    ),
               
    url(
      regex=r'^product/delete/(?P<pk>[\d]+)/$',
      view = ProductDeleteView.as_view(),
      name = 'Product_Delete'  
    ),
                  
]
