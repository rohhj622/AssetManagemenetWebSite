# controller
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from signup.models import Member
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def searchID(request):
    data_dic = {}

    if request.method == 'GET':
        m_id = request.GET.get('m_id')

        try:
            is_exist = Member.objects.filter(m_id__contains=m_id)
            data_dic['mem_list'] = is_exist
            print(is_exist)
        except ObjectDoesNotExist:
            pass

    return render(request, 'searchID/searchResult.html', data_dic)
