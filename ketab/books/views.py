from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def home(request):
    return render(request,
                  'books/home.html',
                  {})

def booklist(request):
    books = Book.objects.all()
    return render(request,
                  'books/books_list.html',
                  {'books': books})

