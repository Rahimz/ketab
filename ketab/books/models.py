from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=1500,
                            verbose_name='Name')
    slug = models.SlugField(unique=True,
                            verbose_name='Slug')

    
    def __str__(self):
        return self.name