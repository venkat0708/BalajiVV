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
        regex=r'^commissionPayOuts/$',
        view=views.PayCommissionOrSalary_Index,
        name='PayCommissionOrSalary_Index'
        ),
    url(
      regex=r'^commissionPayOuts/add/$',
      view = views.PayCommissionOrSalary_Add,
      name = 'PayCommissionOrSalary_Add'
    ),

    url(
      regex=r'^commissionPayOuts/update/(?P<id>[\d]+)/$',
      view = views.PayCommissionOrSalary_Update,
      name = 'PayCommissionOrSalary_Update'
    ),

    url(
        regex=r'^commissionPayOuts/(?P<id>[0-9]+)/$',
        view=views.PayCommissionOrSalary_Detail,
        name='PayCommissionOrSalary_Detail'
        ),

    url(
      regex=r'^commissionPayOuts/delete/(?P<id>[\d]+)/$',
      view = views.PayCommissionOrSalary_Delete,
      name = 'PayCommissionOrSalary_Delete'
    ),

    url(
        regex=r'invoices/$',
        view=views.Invoice_Index,
        name = 'Invoice_Index'
        ),

    url(
        regex=r'invoices/update/(?P<id>[\d]+)/$',
        view=views.Invoice_Update,
        name = 'Invoice_Update'
        ),

    url(
        regex=r'invoices/delete/(?P<id>[\d]+)/$',
        view=views.Invoice_Delete,
        name = 'Invoice_Delete'
        ),
    url(
        regex=r'commissions/$',
        view=views.Commission_Index,
        name = 'Commission_Index'
        ),

    url(
        regex=r'commissions/add/$',
        view=views.Commission_Add,
        name = 'Commission_Add'
        ),

    url(
        regex=r'commissions/update/(?P<id>[\d]+)/$',
        view=views.Commission_Update,
        name = 'Commission_Update'
        ),

    url(
        regex=r'commissions/delete/(?P<id>[\d]+)/$',
        view=views.Commission_Delete,
        name = 'Commission_Delete'
        ),


]
