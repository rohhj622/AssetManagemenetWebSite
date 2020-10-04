from django.urls import path
from . import views

urlpatterns =[
    path('', views.signupMain),
    path('setRate/', views.setRate),
    path('registMem/', views.registMem)
]