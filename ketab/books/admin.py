from django.contrib import admin
from.models import Book, Author, Critique, Collection


class AutorshipInline(admin.TabularInline):
    model = Author.books.through


# class CritiqueInline(admin.TabularInline):
    # model = Critique.book.through

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}
    inlines = [AutorshipInline, ]
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    
    
@admin.register(Critique)
class CritiqueAdmin(admin.ModelAdmin):
    list_display = ['author', 'book']
    

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'item_quantity']
    # TODO:: this dkango admin should present a list of books in this collection
