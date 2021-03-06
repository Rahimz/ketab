﻿from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),

    path('books/', views.BookList, name='book_list'),
    path('books/<int:isbn>/', views.BookDetail, name='book_detail'),
    path('books/create/', views.BookCreate.as_view(), name='book_create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),

    path('books/collections/', views.collectionlist, name='collectionlist'),
    path('books/collections/<int:pk>/', views.collectiondetail, name='collectiondetail'),

    path('isbn/', views.IsbnList.as_view(), name='isbn_list'),
    path('isbn/<int:isbn>', views.IsbnDetail, name='isbn_detail'),
    path('isbn/create/', views.IsbnCreate.as_view(), name='isbn-create'),
    path('isbn/<int:isbn>/update/', views.IsbnUpdate, name='isbn_update'),
    path('isbn/<int:isbn>/delete/', views.IsbnDelete, name='isbn_delete'),

    path('authors/', views.AuthorList.as_view(), name='author_list'),
    path('authors/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('authors/<int:pk>/', views.AuthorDetail, name='author_detail'),

    path('translators/', views.TranslatorList.as_view(), name='translator_list'),
    path('translators/create/', views.TranslatorCreate.as_view(), name='translator_create'),
    path('translators/<int:pk>/', views.TranslatorDetail, name='translator_detail'),

    path('illustrator/', views.IllustratorList.as_view(), name='illustrator_list'),
    path('illustrator/create/', views.IllustratorCreate.as_view(), name='illustrator_create'),
    path('illustrator/<int:pk>/', views.IllustratorDetail, name='illustrator_detail'),

    path('shoora/', views.ShooraList.as_view(), name='shoora_list'),
    path('shoora/<int:pk>/', views.ShooraDetail, name='shoora_detail'),
    path('shoora/create/', views.ShooraCreate.as_view(), name='shoora_create'),

    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),
    path('publisher/create/', views.PublisherCreate.as_view(), name='publisher_create'),
    path('publisher/<int:pk>', views.PublisherDetail, name='publisher_detail'),
    ]
