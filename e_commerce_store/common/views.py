from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from e_commerce_store.common.forms import ContactCreateForm
from e_commerce_store.common.models import Contact


# Create your views here.


def landing_page(request):
    return render(request, 'common/index.html')


def about_page(request):
    return render(request, 'common/about.html')


def news_page(request):
    return render(request, 'news/news.html')


class ContactForm(views.CreateView):
    template_name = 'common/contact.html'
    model = Contact
    form_class = ContactCreateForm
    success_url = reverse_lazy('landing-page')
