from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.views import generic


from .models import Category

# Create your views here.

class CategoryIndexView(generic.ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'category_list'
    

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'categories/category_detail.html'
    context_object_name = 'category'
    
    
class CategoryCreateView(generic.edit.CreateView):
    model = Category
    fields = ['name','description']
    template_name = 'categories/category_add.html'
    
    def get_success_url(self):
        return reverse('products:Category_Index')
    
    
class CategoryUpdateView(generic.edit.UpdateView):
    model = Category
    fields = ['name','description']
    template_name = 'categories/category_update.html'
    
    
class CategoryDeleteView(generic.edit.DeleteView):
    model = Category
    template_name = 'categories/category_delete.html'
    success_url = reverse_lazy('products:Category_Index')