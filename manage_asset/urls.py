from django.urls import path
from . import views

urlpatterns =[
    path('', views.new_asset),
    path('cal', views.cal_asset),
]