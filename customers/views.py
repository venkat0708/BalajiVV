from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Customer, Vendor
from .forms import CustomerForm, VendorForm
# Create your views here.


def Permission_Check(user):
	
	return 'customer management' in [i.name for i in user.groups.all()]


@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Index(request):
	customers = Customer.objects.all()
	return render(request, 'customers/index.html',{'customers':customers})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Add_Customer(request):
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('customers:index'))
	else:
		form = CustomerForm()
	return render(request, 'customers/add.html',{'form':form})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Update_Customer(request,id):
	customer = get_object_or_404(Customer,pk=id)
	form = CustomerForm(request.POST or None,instance = customer)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('customers:index'))
	return render(request, 'customers/update.html',{'form':form, 'id':customer.id})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Detail_Customer(request, id):
	customer = get_object_or_404(Customer,pk=id)
	return render(request, 'customers/detail.html', {'customer': customer})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Delete_Customer(request,id):
	customer = get_object_or_404(Customer,pk=id)
	
	if request.method == 'POST':
		form = CustomerForm(request.POST or None, instance=customer)
		
		if form.is_valid():
			customer.delete()
			return HttpResponseRedirect(reverse('customers:index'))
	else:
		form = CustomerForm(instance = customer)
	return render(request, 'customers/delete.html', {'form': form, 'id':id})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Vendor_Index(request):
	vendors = Vendor.objects.all()
	return render(request, 'vendors/index.html',{'vendors':vendors})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Add_Vendor(request):
	if request.method == 'POST':
		form = VendorForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('customers:vendors'))
	else:
		form = VendorForm()
	return render(request, 'vendors/add.html',{'form':form})


@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Update_Vendor(request,id):
	vendor = get_object_or_404(Vendor,pk=id)
	form = VendorForm(request.POST or None,instance = vendor)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('customers:vendors'))
	return render(request, 'vendors/update.html',{'form':form, 'id':id})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Detail_Vendor(request, id):
	vendor = get_object_or_404(Vendor,pk=id)
	return render(request, 'vendors/detail.html', {'vendor': vendor})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Delete_Vendor(request,id):
	vendor = get_object_or_404(Vendor,pk=id)
	
	if request.method == 'POST':
		form = VendorForm(request.POST or None, instance=vendor)
		
		if form.is_valid():
			vendor.delete()
			return HttpResponseRedirect(reverse('customers:vendors'))
	else:
		form = VendorForm(instance = vendor)
	return render(request, 'vendors/delete.html', {'form': form, 'id':id})

