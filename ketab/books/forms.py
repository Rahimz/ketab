from django.forms import ModelForm
from .models import Book, ISBN


class IsbnFormUpdate(ModelForm):

    class Meta:
        model = ISBN
        fields = '__all__'


class BookFormUpdate(ModelForm):

    class Meta:
        model = Book
        fields = '__all__'


