from django.contrib import admin

from .models import Customer, Vendor
# Register your models here.

admin.site.register(Customer, admin.ModelAdmin)

admin.site.register(Vendor, admin.ModelAdmin)
