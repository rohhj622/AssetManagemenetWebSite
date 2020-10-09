from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

import sys
from signup.models import Member
from django.db.models import Q


# Create your views here.


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin/signinMain.html')

    if request.method == "POST":

        m_id = request.POST.get('m_id')  # id
        m_pw = request.POST.get('m_pw')  # passwd

        print(m_id, m_pw)

        is_true = Member.objects.all().filter(Q(m_id=m_id) & Q(m_pw=m_pw)).count()

        if is_true == 1:
            request.session['m_id'] = m_id
            return redirect('/')

        elif is_true == 0:
            return render(request, 'main_page/main.html')

