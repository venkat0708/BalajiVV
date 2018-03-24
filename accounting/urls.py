from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^payins/$',
        view=views.Payins_Index,
        name='Payin_Index'
    ),

    url(
        regex=r'^payins/(?P<id>[0-9]+)/$',
        view=views.Payin_Detail,
        name='Payin_Detail'
        ),
    url(
      regex=r'^payins/add/$',
      view = views.Payin_Add,
      name = 'Payin_Add'
    ),

    url(
      regex=r'^payins/update/(?P<id>[\d]+)/$',
      view = views.Payin_Update,
      name = 'Payin_Update'
    ),

    url(
      regex=r'^payins/delete/(?P<id>[\d]+)/$',
      view = views.Payin_Delete,
      name = 'Payin_Delete'
    ),

    url(
        regex=r'invoices/$',
        view=views.Invoice_Index,
        name = 'Invoice_Index'
        ),
    url(
        regex=r'commissions/$',
        view=views.Commission_Index,
        name = 'Commission_Index'
        ),

]
