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

        # # 만약 아이디랑 페스워드가 맞다면? 1, 아니면 0
        # is_true = Member.objects.all().filter(Q(m_id=m_id) & Q(m_pw=m_pw)).count()
        #
        # print(is_true)
        #
        # if is_true == 1:
        #     # 세션에 값 추가
        #     # request.session['m_id'] = m_id
        #     # 여기엔 직접 url을 적어야함
        #
        #     # if request.session.get('m_id'):
        #     #     print(request.session.get('m_id'))
        # #     #     del (request.session.get['m_id'])
        # #
        # #     return redirect('/')  # 여기엔 직접 url을 적어야함
        #
        # elif is_true == 0:
        #     return render(request, 'signin/signinResult.html')
