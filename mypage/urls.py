from django.urls import path
from . import views

urlpatterns =[
    path('', views.mypageOpen, name='mypageOpening'),
    path('yourpage', views.yourpageOpen),
]