from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Book, Author, Critique, Collection, ISBN, Market, Shoora
from .forms import IsbnFormUpdate


def home(request):
    return render(request,
                  'books/home.html',
                  {})


def booklist(request):
    books = Book.objects.all()
    return render(request,
                  'books/books_list.html',
                  {'books': books})


def bookdetail(request, isbn):
    isbn = get_object_or_404(ISBN,
                             code=isbn)
    book = Book.objects.all().get(isbn=isbn)
    critiques = Critique.objects.filter(book=book)
    collection = Collection.objects.filter(name=book.collection)
    try:
        market = Market.objects.all().get(isbn=isbn)
        shoora = Shoora.objects.all().get(isbn=isbn)
    except Market.DoesNotExist:
        market = None
    except Shoora.DoesNotExist:
        shoora = None
                                       
    return render(request,
                  'books/book_detail.html',
                  {'book': book,
                   'critiques': critiques,
                   'collection': collection,
                   'market': market,
                   'shoora': shoora})


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

class IsbnList(ListView):
    model = ISBN


def IsbnDetail(request, isbn):
    isbn = get_object_or_404(ISBN,
                             code=isbn)
    try:
        book = Book.objects.get(isbn=isbn)
    except Book.DoesNotExist:
        book = None

    return render(request,
                  'books/isbn_detail.html',
                  {'isbn': isbn,
                   'book': book})



class IsbnCreate(CreateView):
    model = ISBN
    fields = '__all__'
    success_url = reverse_lazy('isbn_list')


def IsbnUpdate(request, isbn):
    # TODO: I want to make a feature for staffs to edit isbn
    # the problem is when you edit the isbn and update it the url
    # is not exist so it could not find the isbn_detail.
    # so the url should use a solid way
    isbn_instance = get_object_or_404(ISBN, code=isbn)


    if request.method == 'POST':
        form = IsbnFormUpdate(instance=isbn_instance,
                              data=request.POST)
        if form.is_valid():
            new_isbn = form.save(commit=False)
            new_isbn.code = form.isbn
            new_isbn.save()
            return render(request,
                          'books/isbn_detail.html',
                          {'isbn': new_isbn})

    else:
        form = IsbnFormUpdate(instance=isbn_instance)
    return render(request,
                  'books/isbn_update.html',
                  {'form': form})




class IsbnDelete(DeleteView):
    model = ISBN
    success_url = reverse_lazy('isbn_list')


class AuthorList(ListView):
    model = Author