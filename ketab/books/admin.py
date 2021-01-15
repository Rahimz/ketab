from django.contrib import admin
from.models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']