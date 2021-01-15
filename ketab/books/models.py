from django.db import models
from django.urls import reverse 

class Book(models.Model):
    name = models.CharField(max_length=1500,
                            verbose_name='Name')
    slug = models.SlugField(unique=True,
                            verbose_name='Slug',
                            allow_unicode=True)

    
    def __str__(self):
        return self.name
        
    
    def get_absolute_url(self):
        return reverse('bookdetail', args=[self.pk])
