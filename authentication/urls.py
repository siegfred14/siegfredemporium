from re import L
from django.urls import path
from django.urls import path
from .views import RegisterView, LoginView


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view())
]
