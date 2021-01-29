from django.db import models
from django.urls import reverse 


class Author(models.Model):
    name = models.CharField(max_length=1500,)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Translator(models.Model):
    name = models.CharField(max_length=1500)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Illustrator(models.Model):
    name = models.CharField(max_length=1500)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=1500)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=2500, )
    item_quantity = models.IntegerField()

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('collectiondetail', args=[self.pk])

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=1500,
                            verbose_name='Name')
    slug = models.SlugField(unique=True,
                            verbose_name='Slug',
                            allow_unicode=True)
    isbn = models.IntegerField(blank=True, null=True,)

    author_1 = models.ForeignKey(Author,
                                 related_name='author_1',
                                 blank=True, null=True,
                                 on_delete=models.CASCADE)
    author_2 = models.ForeignKey(Author,
                                 related_name='author_2',
                                 blank=True, null=True,
                                 on_delete=models.CASCADE)

    translator_1 = models.ForeignKey(Translator,
                                     related_name='translator_1',
                                     blank=True, null=True,
                                     on_delete=models.CASCADE)
    translator_2 = models.ForeignKey(Translator,
                                     related_name='translator_2',
                                     blank=True, null=True,
                                     on_delete=models.CASCADE)
    illustrated = models.BooleanField(default=False)
    illustrator_1 = models.ForeignKey(Illustrator,
                                      blank=True, null=True,
                                      related_name='illustrator_1',
                                      on_delete=models.CASCADE)
    illustrator_2 = models.ForeignKey(Illustrator,
                                      blank=True, null=True,
                                      related_name='illustrator_2',
                                      on_delete=models.CASCADE)

    editor = models.CharField(max_length=1500,
                              blank=True)
    re_write = models.CharField(max_length=1500,
                                blank=True)
    collector = models.CharField(max_length=1500,
                                 blank=True)
    is_collection = models.BooleanField(default=False)
    collection = models.ForeignKey(Collection,
                                   blank=True,
                                   null=True,
                                   on_delete=models.CASCADE,
                                   related_name='book')
    number = models.IntegerField(blank=True, null=True,)
    pub_place = models.CharField(max_length=1500,
                                 blank=True, null=True,)
    publisher = models.ForeignKey(Publisher,
                                  related_name='publisher',
                                  blank=True, null=True,
                                  on_delete=models.CASCADE)
    publisher_sub_cat = models.CharField(max_length=1500,
                                         blank=True, null=True,)
    publisher2 = models.ForeignKey(Publisher,
                                   related_name='publisher2',
                                   blank=True, null=True,
                                   on_delete=models.CASCADE)
    pub_year = models.IntegerField(blank=True, null=True,)
    pages = models.IntegerField(blank=True, null=True,)
    circulation = models.IntegerField(blank=True, null=True,)
    bibliography = models.CharField(max_length=1500,
                                    blank=True, null=True,)

    tags = models.CharField(max_length=1500,
                            blank=True, null=True,)
    genre = models.CharField(max_length=1500,
                             blank=True, null=True,)

    created_date = models.DateTimeField(auto_now_add=True,
                                        blank=True, null=True,)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bookdetail', args=[self.pk])

  
class Critique(models.Model): 
    author = models.CharField(max_length=1500,)
    content = models.TextField()
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             related_name='critique')
    
    def __str__(self):
        return " : ".join([self.author, self.book.name])
