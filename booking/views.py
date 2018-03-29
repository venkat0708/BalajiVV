from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone

from .models import Event,Booked_Service
from .forms import Booked_Service_Form
from accounting.forms import PayinForm


class EventIndexView(LoginRequiredMixin,UserPassesTestMixin,generic.ListView):
    model = Event
    template_name = 'booking/event_list.html'
    context_object_name = 'events_list'
    login_url = '/'

    def test_func(self):
        return  'event management' in [i.name for i in self.request.user.groups.all()]


class EventDetailView(LoginRequiredMixin,UserPassesTestMixin,generic.DetailView):
    model = Event
    template_name = 'booking/event_detail.html'
    context_object_name = 'event'
    login_url = '/'

    def test_func(self):
        return  'event management' in [i.name for i in self.request.user.groups.all()]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # add booked service form
        bsf = Booked_Service_Form(initial = {'event':self.object})
        try:
            amt= self.object.invoice.all()[0].amount - self.object.invoice.all()[0].paid
        except:
            amt = 0
        pf = PayinForm(initial = {
                'event':self.object,
                'customer':self.object.customer,
                'date':timezone.now().date(),
                'time':timezone.now().time(),
                'amount': amt
                })

        context['booked_service_form'] = bsf
        context['Payin_form'] = pf
        return context


class EventCreateView(LoginRequiredMixin, UserPassesTestMixin,generic.edit.CreateView):
    model = Event
    fields = ['customer','venue', 'city','start_date', 'start_time','end_date','end_time','advance','status']
    template_name = 'booking/event_add.html'
    login_url = '/'

    def test_func(self):
        return  'event management' in [i.name for i in self.request.user.groups.all()]

    def get_success_url(self):
        return reverse('booking:Event_Index')

    def test_func(self):
        print (self.request.user.groups.all())
        return  'event management' in [i.name for i in self.request.user.groups.all()]


class EventUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.edit.UpdateView):
    model = Event
    fields = ['customer','venue', 'city','start_date', 'start_time','end_date','end_time','advance','status']
    template_name = 'booking/event_update.html'
    login_url = '/'

    def test_func(self):
        return  'event management' in [i.name for i in self.request.user.groups.all()]

class EventDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.edit.DeleteView):
    model = Event
    template_name = 'booking/event_delete.html'
    success_url = reverse_lazy('booking:Event_Index')
    login_url = '/'

    def test_func(self):
        return  'event management' in [i.name for i in self.request.user.groups.all()]


def Permission_Check(user):

	return 'event management' in [i.name for i in user.groups.all()]

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Booked_Service_Index(request):
	booked_services = Booked_Service.objects.all()
	return render(request, 'booked_services/booked_services_list.html',{'booked_services':booked_services})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Booked_Service_Add(request):
	if request.method == 'POST':
		form = Booked_Service_Form(request.POST)
		if form.is_valid():
			service = form.save()
			return HttpResponseRedirect(reverse('booking:Event_Detail', kwargs={'pk':service.event.id}))
	else:
		form = Booked_Service_Form()
	return render(request, 'booked_services/booked_services_add.html',{'form':form})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Booked_Service_Update(request,id):
	booked_service = get_object_or_404(Booked_Service,pk=id)
	form = Booked_Service_Form(request.POST or None,instance = booked_service)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('booking:Booked_Service_Index'))
	return render(request, 'booked_services/booked_services_update.html',{'form':form, 'id':booked_service.id})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Booked_Service_Detail(request, id):
    booked_service= get_object_or_404(Booked_Service,pk=id)
    return render(request, 'booked_services/booked_services_detail.html', {'booked_service': booked_service})

@login_required
@user_passes_test(Permission_Check,redirect_field_name= None)
def Booked_Service_Delete(request,id):
	booked_service = get_object_or_404(Booked_Service,pk=id)

	if request.method == 'POST':
		form = Booked_Service_Form(request.POST or None, instance=booked_service)

		if form.is_valid():
			booked_service.delete()
			return HttpResponseRedirect(reverse('booking:Booked_Service_Index'))
	else:
		form = Booked_Service_Form(instance = booked_service)
	return render(request, 'booked_services/booked_service_delete.html', {'form': form, 'id':id})
