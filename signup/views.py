# like controller

from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def signupMain(request):
    if request.method == 'GET':
        return render(request, 'signup/signUpMain.html')


def setRate(request):
    if request.method == "POST":
        n_m_id = request.POST.get('m_id')
        n_m_pw = request.POST.get('m_pw')
        n_m_name = request.POST.get('m_name')
        print(n_m_name,n_m_id,n_m_pw)

        new_mem = {'m_id': n_m_id, 'm_pw': n_m_pw, 'm_name': n_m_name}

        return render(request, 'signup/setRate.html', new_mem)


def registMem(request):
    if request.method == 'POST':
        m_id = request.POST.get('m_id')
        m_pw = request.POST.get('m_pw')
        m_name = request.POST.get('m_name')
        m_sdrate = request.POST.get('m_sdrate')
        m_srate = request.POST.get('m_srate')
        m_frate = request.POST.get('m_frate')

        new_mem = Member(m_id=m_id, m_pw=m_pw, m_name=m_name,
                         m_sdrate=m_sdrate, m_srate=m_srate, m_frate=m_frate)

        # db insert
        new_mem.save()
        return HttpResponse('hellpo')