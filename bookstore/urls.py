from django.urls import path

from bookstore.views import HomeView, ReviewsListView, LoginFormView, RegistrationFormView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path("reviews/", ReviewsListView.as_view(), name='reviews'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('register/', RegistrationFormView.as_view(), name='register')
]