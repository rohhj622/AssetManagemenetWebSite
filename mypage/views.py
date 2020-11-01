from django.shortcuts import render
from django.http import HttpResponse
from signup.models import Member
from .models import Asset
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Count


# Create your views here.
def mypageOpen(request):
    m_id = request.user.get_username()

    if request.method == 'GET':
        if Asset.objects.filter().order_by('-a_id'):  # 차있다면

            # 전체 데이터 담아서 보낼 리스트
            all_data = []
            # 지난 자산 현황 축적할 딕셔너리
            acc_tot = {}

            """
                1. 현재 아이디 정보를 보내야함(기본 정보들 있는 거)
                2. 지난 자산 현황을 보내야함(총합)
                    2-1. 현재 자산 비율 계산해야함, 이것도 총합 계산
                    2-2. 과거 자산 각각 총합 계산
                3. 현재 자산 비율이 이상적인 비율을 맞추기 위한 금액을 계산해야 함
            """

            # 1. 지금 현재 아이디의 기본 정보 가져옴. (비율들도 o)
            mem = Member.objects.filter(m_id=m_id).values()[0]
            print(mem)

            # 현재 아이디의 기본 정보 all_data 에 append
            all_data.append(mem)

            # 2. Asset 에 있는 아이디 의 자산 정보 모두 가져옴 오름차순 정렬 (현재가 맨 앞에 오게)
            assets = Asset.objects.filter(m_id=m_id).order_by('a_datetime').values()

            # 총 자산 금액, 각각 자산금액 현황
            for i in range(0, len(assets)):

                # 2-1. 현재 자산금액과 비율을 계산함. //가장 최근 내용
                if i == len(assets)-1:
                    # 제일 최근 걸로 비율 계산
                    saving = int(assets[i]['a_saving'])
                    deposit = int(assets[i]['a_deposit'])
                    stock = int(assets[i]['a_stock'])
                    fund = int(assets[i]['a_fund'])

                    total = saving + deposit + stock + fund

                    # 지난 자산 현황을 나타내기 위한 딕셔너리에 전체 금액을 추가함
                    acc_tot[str(assets[i]['a_datetime'])] = total

                    r_sa = int((saving + deposit) / total * 100)  # 예적금 비율
                    r_st = int(stock / total * 100)  # 주식 비율
                    r_fu = int(100 - r_sa - r_st)  # 펀드 비율

                    # 현재 비율 딕셔너리
                    mem_c_rate = {'r_sa': r_sa, 'r_st': r_st, 'r_fu': r_fu}

                    # 모든 데이터를 담을 리스트에 추가
                    all_data.append(mem_c_rate)
                    print(r_sa, r_st, r_fu)

                # 2-2.과거 자산들 비율 계산 없이 그냥 총합만 계산
                else:
                    total = assets[i]['a_saving'] + assets[i]['a_deposit']\
                            + assets[i]['a_stock']+assets[i]['a_fund']

                    # 지난 자산 현황을 나타내기 위한 딕셔너리에 전체 금액을 추가함
                    acc_tot[str(assets[i]['a_datetime'])] = total

            print(acc_tot)
            all_data.append(assets)

            print(all_data)
            return render(request, 'mypage/mypage.html', mem)
        else:  # 비었다면
            return render(request, 'manage_asset/new_asset.html')

    if request.method == "POST":
        a_saving = request.POST.get('a_saving')
        a_deposit = request.POST.get('a_deposit')
        a_stock = request.POST.get('a_stock')
        a_fund = request.POST.get('a_fund')

        new_asset = Asset(m_id=m_id, a_saving=a_saving, a_deposit=a_deposit,
                          a_stock=a_stock, a_fund=a_fund)
        new_asset.save()  # 자산 저장

        m_name = Member.objects.filter(m_id=request.user.get_username()).values()[0]
        # u_name = str(m_name[0]['m_name'])

        return render(request, 'mypage/mypage.html', m_name)

