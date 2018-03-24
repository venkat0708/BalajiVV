from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.db.models import F

from .models import Payin, Invoice, Commission
from .forms import PayinForm


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


def Invoice_Index(request):
	invoices = Invoice.objects.all().annotate(due_amount =F('amount') - F('paid'))
	return render(request,'commissions/invoices_index.html', {'invoices':invoices})

def Commission_Index(request):
	commissions = Commission.objects.all().annotate(due_amount =F('amount') - F('paid'))
	return render(request, 'commissions/commissions_index.html', {'commissions': commissions})
