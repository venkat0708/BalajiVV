from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin


from .models import Category

# Create your views here.

class CategoryIndexView(LoginRequiredMixin,UserPassesTestMixin,generic.ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'category_list'
    login_url = '/'
    
    def test_func(self):
        return  'product management' in [i.name for i in self.request.user.groups.all()]
    

class CategoryDetailView(LoginRequiredMixin,UserPassesTestMixin,generic.DetailView):
    model = Category
    template_name = 'categories/category_detail.html'
    context_object_name = 'category'
    login_url = '/'
    
    def test_func(self):
        return  'product management' in [i.name for i in self.request.user.groups.all()]
    
    
class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin,generic.edit.CreateView):
    model = Category
    fields = ['name','description']
    template_name = 'categories/category_add.html'
    login_url = '/'
    
    def test_func(self):
        return  'product management' in [i.name for i in self.request.user.groups.all()]
    
    def get_success_url(self):
        return reverse('products:Category_Index')
    
    def test_func(self):
        print self.request.user.groups.all()
        return  'product management' in [i.name for i in self.request.user.groups.all()]
    
    
class CategoryUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.edit.UpdateView):
    model = Category
    fields = ['name','description']
    template_name = 'categories/category_update.html'
    login_url = '/'
    
    def test_func(self):
        return  'product management' in [i.name for i in self.request.user.groups.all()]
    
class CategoryDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.edit.DeleteView):
    model = Category
    template_name = 'categories/category_delete.html'
    success_url = reverse_lazy('products:Category_Index')
    login_url = '/'
    
    def test_func(self):
        return  'product management' in [i.name for i in self.request.user.groups.all()]