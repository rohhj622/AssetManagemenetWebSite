from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.template import RequestContext


def signout(request):
    logout(request)
    return redirect('/')