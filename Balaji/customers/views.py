from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin

from .models import Customer, Vendor, Staff
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


class StaffIndexView(LoginRequiredMixin,UserPassesTestMixin,generic.ListView):
    model = Staff
    template_name = 'staff/staff_list.html'
    context_object_name = 'staff_list'
    login_url = '/'

    def test_func(self):
        return  'staff management' in [i.name for i in self.request.user.groups.all()]


class StaffDetailView(LoginRequiredMixin,UserPassesTestMixin,generic.DetailView):
    model = Staff
    template_name = 'staff/staff_detail.html'
    context_object_name = 'staff'
    login_url = '/'

    def test_func(self):
        return  'staff management' in [i.name for i in self.request.user.groups.all()]


class StaffCreateView(LoginRequiredMixin, UserPassesTestMixin,generic.edit.CreateView):
    model = Staff
    fields = ['name','address','city','phone_number','is_active']
    template_name = 'staff/staff_add.html'
    login_url = '/'

    def test_func(self):
        return  'staff management' in [i.name for i in self.request.user.groups.all()]

    def get_success_url(self):
        return reverse('customers:Staff_Index')

    def test_func(self):
        print (self.request.user.groups.all())
        return  'staff management' in [i.name for i in self.request.user.groups.all()]


class StaffUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.edit.UpdateView):
    model = Staff
    fields = ['name','address','city','phone_number','is_active']
    template_name = 'staff/staff_update.html'
    login_url = '/'

    def test_func(self):
        return  'staff management' in [i.name for i in self.request.user.groups.all()]

class StaffDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.edit.DeleteView):
    model = Staff
    template_name = 'staff/staff_delete.html'
    success_url = reverse_lazy('customers:Staff_Index')
    login_url = '/'

    def test_func(self):
        return  'staff management' in [i.name for i in self.request.user.groups.all()]
