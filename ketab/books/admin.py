from django.contrib import admin
from.models import Book, Author, Critique, Collection, \
    Illustrator, Publisher, Translator, ISBN, \
    Market, Prize, BookGroup, Shoora, Content


# class AutorshipInline(admin.TabularInline):
#     model = Author.books.through


# class CritiqueInline(admin.TabularInline):
#     model = Critique.book.through


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author_1', 'isbn', 'publisher']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ISBN)
class ISBNAdmin(admin.ModelAdmin):
    list_display = ['code']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Translator)
class TranslatorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Illustrator)
class IllustratorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Critique)
class CritiqueAdmin(admin.ModelAdmin):
    list_display = ['author', 'book']
    

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'item_quantity']
    # TODO:: this django admin should present a list of books in this collection


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ['isbn', 'available']


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'latin_name']


@admin.register(BookGroup)
class BookGroupAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Shoora)
class ShooraAdmin(admin.ModelAdmin):
    list_display = ['isbn', ]


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['author', 'book']