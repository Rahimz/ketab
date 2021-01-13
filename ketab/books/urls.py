from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.booklist, name='booklist'),
    path('books/<int:pk>', views.bookdetail, name='bookdetail'),
    ]
