# like controller

from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup/signUpMain.html')

    if request.method == "POST":
        m_id = request.POST.get('m_id')
        m_pw = request.POST.get('m_pw')
        m_name = request.POST.get('m_name')
        m_sdrate = request.POST.get('m_sdrate')
        m_srate = request.POST.get('m_srate')
        m_frate = request.POST.get('m_frate')
        print(m_name, m_id, m_pw)

        new_mem = Member(m_id=m_id, m_pw=m_pw, m_name=m_name,
                         m_sdrate=m_sdrate, m_srate=m_srate, m_frate=m_frate)

        # db insert
        new_mem.save()

        return render(request, 'signup/setRate.html')
