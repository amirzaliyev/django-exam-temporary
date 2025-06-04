from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView

from .forms import ReviewModelForm, UserModelForm, UserLoginModelForm
from .models import Book, Review


# Create your views here.

class HomeView(ListView):
    template_name = 'bookstore/index.html'
    queryset = Book.objects.all()
    context_object_name = 'books'


class ReviewsListView(ListView):
    template_name = 'bookstore/review.html'
    queryset = Review.objects.all()
    context_object_name = 'reviews'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(
            ratings=Review.Ratings.choices,
            books=Book.objects.all()
        )
        return context


class CreateReview(CreateView):
    template_name = 'bookstore/review.html'
    form_class = ReviewModelForm
    success_url = reverse_lazy('reviews')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class LoginFormView(FormView):
    form_class = UserLoginModelForm
    template_name = 'bookstore/login.html'


class RegistrationFormView(CreateView):
    form_class = UserModelForm
    template_name = 'bookstore/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
