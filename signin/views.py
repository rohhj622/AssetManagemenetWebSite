from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext

import sys
# from signup.models import Member
# from django.db.models import Q
# Create your views here.


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin/signinMain.html')

    if request.method == "POST":

        m_id = request.POST.get('m_id')  # id
        m_pw = request.POST.get('m_pw')  # passwd

        print(m_id, m_pw)
        user = authenticate(username=m_id, password=m_pw)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signin/signinResult.html')
