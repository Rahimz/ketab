from django.db import models
from django.urls import reverse 


class ISBN(models.Model):
    code = models.IntegerField(unique=True)

    def get_absolute_url(self):
        return reverse('isbn_detail', args=[self.pk])

    def __str__(self):
        return str(self.code)


class Author(models.Model):
    name = models.CharField(max_length=1500,)
    latin_name = models.CharField(max_length=1500,
                                  blank=True, null=True)
    nationality = models.CharField(max_length=1500,
                                   blank=True, null=True)

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
    latin_name = models.CharField(max_length=1500,
                                  blank=True, null=True)
    nationality = models.CharField(max_length=1500,
                                   blank=True, null=True)

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


class Prize(models.Model):
    name = models.CharField(max_length=1500,
                            unique=True,)
    latin_name = models.CharField(max_length=1500,
                                  blank=True, null=True)
    organisation = models.CharField(max_length=1500,
                                    blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=1500,
                            verbose_name='Name')
    slug = models.SlugField(unique=True,
                            verbose_name='Slug',
                            allow_unicode=True)
    isbn = models.OneToOneField(ISBN,
                                related_name='isbn',
                                on_delete=models.CASCADE,)

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
    image = models.ImageField(upload_to='books/',
                              blank=True, null=True,)

    created_date = models.DateTimeField(auto_now_add=True,
                                        blank=True, null=True,)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.isbn])

  
class Critique(models.Model): 
    author = models.CharField(max_length=1500,)
    content = models.TextField()
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             related_name='critique')
    
    def __str__(self):
        return " : ".join([self.author, self.book.name])


class Market(models.Model):
    # The market situation has a One to One relation with ISBN which is mean
    # we could not have two or more market situation for a unique ISBN
    isbn = models.OneToOneField(ISBN,
                                related_name='market',
                                on_delete=models.CASCADE)
    available = models.BooleanField(default=False)
    last_price = models.DecimalField(max_digits=10, decimal_places=2,
                                     blank=True, null=True,)
    # TODO:: year field should be automatic list
    last_published_year = models.IntegerField(blank=True, null=True,)
    last_circulation = models.IntegerField(blank=True, null=True,)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.isbn)


class BookGroup(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Shoora(models.Model):
    """
    This Shoora class is used to grab the data that CBC is created for each book.
    """
    isbn = models.OneToOneField(ISBN,
                                related_name='shoora',
                                on_delete=models.CASCADE)
    book_group = models.ForeignKey(BookGroup,
                                   related_name='book_group',
                                   on_delete=models.CASCADE)
    subject = models.CharField(max_length=1000, blank=True, null='True')
    category = models.CharField(max_length=1000, blank=True, null='True')
    function = models.CharField(max_length=1000, blank=True, null='True')
    property = models.CharField(max_length=1000, blank=True, null='True')
    satiric = models.BooleanField(default=False)
    main_character = models.CharField(max_length=200,
                                      choices=[('human', 'Human'),
                                               ('animal', 'Animal'),
                                               ('other', 'Other')],
                                      default='human')
    main_character_description = models.TextField(blank=True, null=True)
    pov = models.CharField(max_length=1500,
                           blank=True, null=True,
                           verbose_name='Point of view')
    events_place = models.CharField(max_length=1500,
                           blank=True, null=True,)
    child_special_need = models.CharField(max_length=1500,
                                          blank=True, null=True)
    genre = models.CharField(max_length=1000,
                             blank=True, null=True)
    genre_descriptive = models.CharField(max_length=2500,
                                         blank=True, null=True)

    age_from = models.IntegerField(blank=True, null=True)
    age_to = models.IntegerField(blank=True, null=True)

    position = models.CharField(max_length=1500,
                                blank=True, null=True)

    book_latin_name = models.CharField(max_length=1500, blank=True, null=True)
    author_latin_name = models.CharField(max_length=1500, blank=True, null=True)
    language = models.CharField(max_length=1500,
                                blank=True, null=True)
    nationality = models.CharField(max_length=1500,
                                   blank=True, null=True)

    # TODO:: final score comes from every content reviews
    score = models.IntegerField(blank=True, null=True)

    # TODO::other translation should be added
    other_translation = models.BooleanField(default=False)

    copyright = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return str(self.isbn)

    def get_absolute_url(self):
        return reverse('shoora_detail', args=[self.pk])


class Content(models.Model):
    author = models.CharField(max_length=500,)
    description = models.TextField()
    book = models.ForeignKey(Shoora,
                             on_delete=models.CASCADE,
                             related_name='content')
    created_date = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.author + ' - ' + str( self.book)