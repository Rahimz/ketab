from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Book, Author, Translator, Critique, Collection, ISBN, Market, Shoora, Illustrator
from news.models import News
from .forms import IsbnFormUpdate, BookFormUpdate


def home(request):
    public_news = News.objects.filter(category='public')[:3]
    staff_news = News.objects.filter(category='staff')[:3]
    admin_news = News.objects.filter(category='admin')[:3]
    return render(request,
                  'books/home.html',
                  {'public_news': public_news,
                   'staff_news': staff_news,
                   'admin_news': admin_news, })


def BookList(request):
    books = Book.objects.all()
    return render(request,
                  'books/books_list.html',
                  {'books': books})


def BookDetail(request, isbn):
    isbn = get_object_or_404(ISBN,
                             code=isbn)
    book = Book.objects.all().get(isbn=isbn)
    market = None
    shoora = None
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


class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('book_list')


class BookUpdate(UpdateView):
    model = Book
    form_class = BookFormUpdate
    template_name = 'books/book_update_form.html'
    success_url = reverse_lazy('book_list')


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


# Author Views
class AuthorList(ListView):
    model = Author


class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('author_list')


def AuthorDetail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = None
    book_id1 = Book.objects.filter(author_1=author).values_list('id', flat=True)
    book_id2 = Book.objects.filter(author_2=author).values_list('id', flat=True)
    book_ids = book_id1 | book_id2
    try:
        books = Book.objects.filter(id__in=book_ids)
    except Book.DoesNotExist:
        books = None

    return render(request,
                  'books/author_detail.html',
                  {'author': author,
                   'books': books})


# Translator Views
class TranslatorList(ListView):
    model = Translator


class TranslatorCreate(CreateView):
    model = Translator
    fields = '__all__'
    success_url = reverse_lazy('translator_list')


def TranslatorDetail(request, pk):
    translator = get_object_or_404(Translator, pk=pk)
    books = None
    book_id1 = Book.objects.filter(translator_1=translator).values_list('id', flat=True)
    book_id2 = Book.objects.filter(translator_2=translator).values_list('id', flat=True)
    book_ids = book_id1 | book_id2
    try:
        books = Book.objects.filter(id__in=book_ids)
    except Book.DoesNotExist:
        books = None

    return render(request,
                  'books/translator_detail.html',
                  {'translator': translator,
                   'books': books})


# Illustrator Views
class IllustratorList(ListView):
    model = Illustrator


class IllustratorCreate(CreateView):
    model = Illustrator
    fields = '__all__'
    success_url = reverse_lazy('illustrator_list')


def IllustratorDetail(request, pk):
    illustrator = get_object_or_404(Illustrator, pk=pk)
    books = None
    '''
    These two query sets check whether the illustrator is the first illustrator of a book
    or is the second illustrator of a book
    '''
    book_id1 = Book.objects.filter(illustrator_1=illustrator).values_list('id', flat=True)
    book_id2 = Book.objects.filter(illustrator_2=illustrator).values_list('id', flat=True)
    book_ids = book_id1 | book_id2  # removes duplicated book names
    try:
        books = Book.objects.filter(id__in=book_ids)
    except Book.DoesNotExist:
        books = None

    return render(request,
                  'books/illustrator_detail.html',
                  {'illustrator': illustrator,
                   'books': books})


# Shoora Views
class ShooraList(ListView):
    model = Shoora


def ShooraDetail(request, pk):
    shoora = get_object_or_404(Shoora, pk=pk)
    book = Book.objects.get(isbn=shoora.isbn)
    # '''
    # These two query sets check whether the illustrator is the first illustrator of a book
    # or is the second illustrator of a book
    # '''
    # book_id1 = Book.objects.filter(illustrator_1=illustrator).values_list('id', flat=True)
    # book_id2 = Book.objects.filter(illustrator_2=illustrator).values_list('id', flat=True)
    # book_ids = book_id1 | book_id2  # removes duplicated book names
    # try:
    #     books = Book.objects.filter(id__in=book_ids)
    # except Book.DoesNotExist:
    #     books = None

    return render(request,
                  'books/shoora_detail.html',
                  {'shoora': shoora,
                   'book': book})


class ShooraCreate(CreateView):
    model = Shoora
    fields = '__all__'
    success_url = reverse_lazy('shoora_list')