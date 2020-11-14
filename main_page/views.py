
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def mainpageOpen(request):
    return render(request, 'main_page/main.html')
    # return render(request, 'main_page/main2.html')