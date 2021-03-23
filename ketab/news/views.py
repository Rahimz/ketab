from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import News


def NewsList(request):
    public_news = News.objects.filter(category='public')
    staff_news = News.objects.filter(category='staff')
    admin_news = News.objects.filter(category='admin')
    return render(request,
                  'news/news_list.html',
                  {'public_news': public_news,
                   'staff_news': staff_news,
                   'admin_news': admin_news, })

# class NewsDetail(DetailView):
#     model = News

def NewsDetail(request, pk):
    news_detail = get_object_or_404(News, pk=pk)
    allowed = False
    if news_detail.category == 'public':
        allowed = True
    if news_detail.category == 'staff' and request.user.is_staff:
        allowed = True
    if news_detail.category == 'admin' and request.user.is_superuser:
        allowed = True
    return render(request,
                  'news/news_detail.html',
                  {'news': news_detail,
                   'allowed': allowed,})
