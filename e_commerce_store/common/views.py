from django.shortcuts import render


# Create your views here.


def landing_page(request):
    return render(request, 'common/index.html')


def about_page(request):
    return render(request, 'common/about.html')


def news_page(request):
    return render(request, 'news/news.html')

