from django.contrib import admin
from.models import Book, Author


class AutorshipInline(admin.TabularInline):
    model = Author.books.through

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}
    inlines = [AutorshipInline,]
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']