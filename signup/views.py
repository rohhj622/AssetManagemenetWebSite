# controller
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User

# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup/signUpMain.html')

    if request.method == "POST":

        m_id = request.POST.get('m_id')  # id
        m_pw = request.POST.get('m_pw')  # passwd
        m_name = request.POST.get('m_name')  # 이름
        m_sdrate = request.POST.get('m_sdrate')  # 예적금비율
        m_srate = request.POST.get('m_srate')  # 주식비율
        m_frate = request.POST.get('m_frate')  # 펀드비율

        print(m_name, m_id, m_pw, m_sdrate, m_srate, m_frate)

        # 자체 DB model
        new_mem = Member(m_id=m_id, m_pw=m_pw, m_name=m_name,
                         m_sdrate=m_sdrate, m_srate=m_srate, m_frate=m_frate)

        # db insert
        new_mem.save()

        # django 제공 user 관리
        user = User.objects.create_user(username=m_id, password=m_pw, first_name=m_name)
        # db 저장
        user.save()

        request.session.flush()

        return render(request, 'signup/signUpResult.html')
