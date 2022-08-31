from django.views.generic import TemplateView
from django.urls import path
from .views import UserLoginView, RegisterPage, MainView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

app_name = 'main'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='main:login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', MainView.as_view(), name='list'),

]