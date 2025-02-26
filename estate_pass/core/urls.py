from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('valid/', views.validate, name='validate'),
    path('register/', views.register, name="signup"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logOut, name="logout"),
    path('valid/all/', views.allFlat, name="all"),
    path('valid/all/<str:pk>', views.aFlat, name="aflat"),
    
]