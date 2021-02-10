from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.booklist, name='booklist'),
    path('books/<int:isbn>/', views.bookdetail, name='bookdetail'),
    path('books/collections/', views.collectionlist, name='collectionlist'),
    path('books/collections/<int:pk>/', views.collectiondetail, name='collectiondetail'),

    path('isbn/', views.IsbnList.as_view(), name='isbn_list'),
    path('isbn/create/', views.IsbnCreate.as_view(), name='isbn-create'),
    path('isbn/<int:pk>/update/', views.IsbnUpdate.as_view(), name='isbn-update'),
    path('isbn/<int:pk>/delete/', views.IsbnDelete.as_view(), name='isbn-delete'),
    ]
