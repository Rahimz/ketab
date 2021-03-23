from django.db import models
from django.urls import reverse


class News(models.Model):
    CATEGORY_CHOICES = (('public', 'Public'),
                        ('staff', 'Staff'),
                        ('admin', 'Admin'))
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100,
                                choices=CATEGORY_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']


