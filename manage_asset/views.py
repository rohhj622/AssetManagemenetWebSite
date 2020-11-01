from django.shortcuts import render
from django.http import HttpResponse
from signup.models import Member
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Count


# Create your views here.
def new_asset(request):
    return render(request, 'manage_asset/new_asset.html')

