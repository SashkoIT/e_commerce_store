from django.urls import path
from e_commerce_store.common.views import *

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('about/', about_page, name='about-page'),
    path('news/', news_page, name='news-page'),
]
