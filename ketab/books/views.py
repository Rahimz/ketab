from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Author, Critique, Collection


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
    authors = book.author_set.all()
    critiques = Critique.objects.filter(book=book)
    collection = Collection.objects.filter(name=book.collection)
                                       
    return render(request,
                  'books/book_detail.html',
                  {'book': book,
                   'authors': authors,
                   'critiques': critiques,
                   'collection': collection})


def collectionlist(request):
    collections = Collection.objects.all()
    return render(request,
                  'books/collections_list.html',
                  {'collections': collections})

  
def collectiondetail(request, pk):
    collection = get_object_or_404(Collection,
                                   pk=pk)
    books = Book.objects.filter(collection=collection)
    return render(request,
                  'books/collection_detail.html',
                  {'collection': collection,
                   'books': books})

