from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('valid/', views.validate, name='home'),
]