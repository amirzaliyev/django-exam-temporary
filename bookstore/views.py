from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Book

# Create your views here.

class HomeView(ListView):
    template_name = 'bookstore/index.html'
    queryset = Book.objects.all()
    context_object_name = 'books'


class ReviewsListView(TemplateView):
    template_name = 'bookstore/review.html'

class LoginFormView(TemplateView):
    template_name = 'bookstore/login.html'

class RegistrationFormView(TemplateView):
    template_name = 'bookstore/register.html'
