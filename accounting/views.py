from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.db.models import F

from .models import Payin, Invoice, Commission, PayCommissionOrSalary
from .forms import PayinForm, PayCommissionOrSalaryForm


def Permission_Check(user):

	return 'accounting management' in [i.name for i in user.groups.all()]

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Payins_Index(request):
    payins = Payin.objects.all()
    return render(request,'payins/Payin_Index.html', {'payins_list':payins})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Payin_Add(request):
	if request.method == 'POST':
		form = PayinForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('accounting:Payin_Index'))
	else:
		form = PayinForm()
	return render(request, 'payins/Payin_Add.html',{'form':form})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Payin_Update(request,id):
	payin = get_object_or_404(Payin,pk=id)
	form = PayinForm(request.POST or None,instance = payin)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('accounting:Payin_Index'))
	return render(request, 'payins/Payin_Update.html',{'form':form, 'id':payin.id})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Payin_Detail(request, id):
	payin = get_object_or_404(Payin,pk=id)
	return render(request, 'payins/Payin_Detail.html', {'payin': payin})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Payin_Delete(request,id):
	payin = get_object_or_404(Payin,pk=id)

	if request.method == 'POST':
		form = PayinForm(request.POST or None, instance=payin)

		if form.is_valid():
			payin.delete()
			return HttpResponseRedirect(reverse('accounting:Payin_Index'))
	else:
		form = PayinForm(instance = payin)
	return render(request, 'payins/Payin_Delete.html', {'form': form, 'id':id})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def PayCommissionOrSalary_Index(request):
    payouts = PayCommissionOrSalary.objects.all()
    return render(request,'payouts_commission/Payout_Commission_Index.html', {'payouts_list':payouts})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def PayCommissionOrSalary_Add(request):
	if request.method == 'POST':
		form = PayCommissionOrSalaryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('accounting:PayCommissionOrSalary_Index'))
	else:
		form = PayCommissionOrSalaryForm()
	return render(request, 'payouts_commission/Payout_Commission_Add.html',{'form':form})


@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def PayCommissionOrSalary_Update(request,id):
	payout = get_object_or_404(PayCommissionOrSalary,pk=id)
	form = PayCommissionOrSalaryForm(request.POST or None,instance = payout)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('accounting:PayCommissionOrSalary_Index'))
	return render(request, 'payouts_commission/Payout_Commission_Update.html',{'form':form, 'id':payout.id})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def PayCommissionOrSalary_Detail(request, id):
	payout = get_object_or_404(PayCommissionOrSalary,pk=id)
	return render(request, 'payouts_commission/Payout_Commission_Detail.html', {'payout': payout})


@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def PayCommissionOrSalary_Delete(request,id):
	payout = get_object_or_404(PayCommissionOrSalary,pk=id)

	if request.method == 'POST':
		form = PayCommissionOrSalaryForm(request.POST or None, instance=payout)

		if form.is_valid():
			payout.delete()
			return HttpResponseRedirect(reverse('accounting:PayCommissionOrSalary_Index'))
	else:
		form = PayCommissionOrSalaryForm(instance = payout)
	return render(request, 'payouts_commission/Payout_Commission_Delete.html', {'form': form, 'id':id})

def Invoice_Index(request):
	invoices = Invoice.objects.all().annotate(due_amount =F('amount') - F('paid'))
	return render(request,'commissions/invoices_index.html', {'invoices':invoices})

def Commission_Index(request):
	commissions = Commission.objects.all().annotate(due_amount =F('amount') - F('paid'))
	return render(request, 'commissions/commissions_index.html', {'commissions': commissions})
