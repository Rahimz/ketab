from django.shortcuts import render, get_object_or_404
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

def bookdetail(request, pk):
    book = get_object_or_404(Book,
                             pk=pk)
    return render(request,
                  'books/book_detail.html',
                  {'book': book})