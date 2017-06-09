from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator, MinValueValidator,MaxValueValidator
from django.core.urlresolvers import reverse

from core.models import BaseEntity

# Create your models here.

class Category(BaseEntity):
    name = models.CharField(
        max_length=80,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z\s]*$',
                 message='name should contain only alphabets',
                code='invalid_name'
            ),
        ]
    )
    description = models.CharField(
        max_length=250,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z\s]*$',
                 message='name should contain only alphabets',
                code='invalid_name'
            ),
        ]
    )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:Category_Detail', kwargs={'pk': self.id})
    
    def get_update_url(self):
        return reverse('products:Category_Update', kwargs={'pk': self.id})
    
    def get_delete_url(self):
        return reverse('products:Category_Delete', kwargs={'pk': self.id})

class Product(BaseEntity):
    name = models.CharField(
        max_length=80,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z\s]*$',
                 message='name should contain only alphabets',
                code='invalid_name'
            ),
        ]
    )
    description = models.CharField(
        max_length=250,
        blank = True,
        null = True,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z\s]*$',
                 message='name should contain only alphabets',
                code='invalid_name'
            ),
        ]
    )
    category = models.ForeignKey(
        'Category',
        models.SET_NULL,
        blank=True,
        null=True,
        related_name = 'products',
    )
    price = models.IntegerField(
        validators=[
            MinValueValidator(
                10,
                message = 'Price should be greater than 10'
            ),
            
            MaxValueValidator(
                100000,
                message = 'Price should be less than 100000'
            ),
        ]
    )
    quantity = models.IntegerField(
        validators=[
            MinValueValidator(
                0,
                message = 'Quantity should be greater than 0'
            ),
            
            MaxValueValidator(
                100000,
                message = 'Quantity should be less than 100000'
            ),
        ]
    )
    
    is_active = models.BooleanField(default =True)
    
    
    def __str__(self):
        return self.name
    
    

class Service(BaseEntity):
    name = models.CharField(
        max_length=80,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z\s]*$',
                 message='name should contain only alphabets',
                code='invalid_name'
            ),
        ]
    )
    description = models.CharField(
        max_length=250,
        blank = True,
        null = True,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z\s]*$',
                 message='name should contain only alphabets',
                code='invalid_name'
            ),
        ]
    )
    category = models.ForeignKey(
        'Category',
        models.SET_NULL,
        blank=True,
        null=True,
        related_name = 'services',
    )
    price = models.IntegerField(
        validators=[
            MinValueValidator(
                10,
                message = 'Price should be greater than 10'
            ),
            
            MaxValueValidator(
                100000,
                message = 'Price should be less than 100000'
            ),
        ]
    )
    
    is_active = models.BooleanField(default =True)
    
    
    def __str__(self):
        return self.name


