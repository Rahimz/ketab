from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('', views.NewsList, name='news_list'),
    # path('<int:pk>/', views.NewsDetail.as_view(), name='news_detail')

    # I want to check the permission of user to show them news and stop finding news based on URL changing
    path('<int:pk>/', views.NewsDetail, name='news_detail')
]