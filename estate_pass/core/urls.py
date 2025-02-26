from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('valid/', views.validate, name='validate'),
    path('register/', views.register, name="signup"),
    path('login/', views.loginPage, name="login"),
]