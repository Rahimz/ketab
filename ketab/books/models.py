from django.db import models
from django.urls import reverse 


class Collection(models.Model):
    name = models.CharField(max_length=2500,)
    item_quantity = models.IntegerField()
    
    
    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=1500,
                            verbose_name='Name')
    slug = models.SlugField(unique=True,
                            verbose_name='Slug',
                            allow_unicode=True)
    collection = models.ForeignKey(Collection,
                                   blank=True,
                                   null=True,
                                   on_delete=models.CASCADE,
                                   related_name='book')
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
        
    
    def get_absolute_url(self):
        return reverse('bookdetail', args=[self.pk])


class Author(models.Model):
    name = models.CharField(max_length=1500,
                            verbose_name='Name')
    books = models.ManyToManyField(Book,
                                   )
        
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
  
  
class Critique(models.Model): 
    author = models.CharField(max_length=1500,)
    content = models.TextField()
    book = models.ForeignKey(Book,
                            on_delete=models.CASCADE,
                            related_name='critique')
    
    
    def __str__(self):
        return " : ".join([self.author, self.book.name])
        
        


