from django.shortcuts import render
from django.shortcuts import redirect
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
        if Asset.objects.filter(m_id=m_id).order_by('-a_id'):  # 차있다면

            # 전체 데이터 담아서 보낼 딕셔너리 (현재 아이디 기본 정보, 현재 자산 비율, 전체 자산 현황//자세함,
            # 지난 자산의 흐름 ,이상적인 자산을 맞추기 위한 가격)
            all_data = {}
            # 지난 자산 현황 축적할 딕셔너리
            acc_tot = {}

            # 현재 자산 비율 딕셔너리
            mem_c_rate = {}

            # 지금 총 자산 딕셔너리
            acc_tot_now = {}

            # 현재  예적금, 주식, 펀드, 총 자산
            cur_asset = [0, 0, 0, 0]

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
            all_data['mem'] = mem

            # 2. Asset 에 있는 아이디 의 자산 정보 모두 가져옴 오름차순 정렬 (현재가 맨 앞에 오게)
            assets = Asset.objects.filter(m_id=m_id).order_by('a_id').values()

            # 총 자산 금액, 각각 자산금액 현황
            for i in range(0, len(assets)):

                # 2-1. 현재 자산금액과 비율을 계산함. //가장 최근 내용
                if i == len(assets)-1:
                    # 제일 최근 걸로 비율 계산
                    saving = int(assets[i]['a_saving'])
                    deposit = int(assets[i]['a_deposit'])
                    stock = int(assets[i]['a_stock'])
                    fund = int(assets[i]['a_fund'])

                    cur_asset[0] = saving + deposit
                    cur_asset[1] = stock
                    cur_asset[2] = fund
                    cur_asset[3] = saving + deposit + stock + fund

                    # 지난 자산 현황을 나타내기 위한 딕셔너리에 전체 금액을 추가함
                    acc_tot[str(assets[i]['a_datetime'])] = cur_asset[3]

                    # 현재 총 자산 딕셔너리
                    acc_tot_now['acc_sd_now'] = cur_asset[0]
                    acc_tot_now['acc_s_now'] = cur_asset[1]
                    acc_tot_now['acc_f_now'] = cur_asset[2]
                    acc_tot_now['acc_tot_now'] = cur_asset[3]
                    print(cur_asset[3])

                    r_sa = int((saving + deposit) / cur_asset[3] * 100)  # 예적금 비율
                    r_st = int(stock / cur_asset[3] * 100)  # 주식 비율
                    r_fu = int(100 - r_sa - r_st)  # 펀드 비율

                    # 현재 비율 딕셔너리
                    mem_c_rate['r_sa'] = r_sa
                    mem_c_rate['r_st'] = r_st
                    mem_c_rate['r_fu'] = r_fu

                    # 모든 데이터를 담을 리스트에 추가 2
                    all_data['mem_c_rate'] = mem_c_rate
                    print(r_sa, r_st, r_fu)

                # 2-2.과거 자산들 비율 계산 없이 그냥 총합만 계산
                else:
                    total = assets[i]['a_saving'] + assets[i]['a_deposit']\
                            + assets[i]['a_stock']+assets[i]['a_fund']
                    print(total)
                    # 지난 자산 현황을 나타내기 위한 딕셔너리에 전체 금액을 추가함
                    acc_tot[str(assets[i]['a_datetime'])] = total

            # all_data.append(assets)
            all_data['acc_tot_now'] = acc_tot_now
            all_data['acc_tot'] = acc_tot

            # 현재 자산 비율을 이상적인 비율을 맞추기 위해서 해야할 것
            # 필요한 거  : 현재 비율, 현재 가격, 현재 총합, 이상 비율, 이상 비율에 맞춘 가격

            idle_asset = {}

            # 이상 비율에 맞춘 가격 구하기  (비율 * 전체 / 100)
            idle_sd = mem['m_sdrate'] * cur_asset[3] / 100  # 이상적인 예적금 가격
            print(idle_sd)
            idle_s = mem['m_srate'] * cur_asset[3] / 100  # 이상적인 주식 가격
            idle_f = mem['m_frate'] * cur_asset[3] / 100  # 이상적인 펀드 가격

            idle_asset['sub_idle_sd'] = int(idle_sd - cur_asset[0])
            idle_asset['sub_idle_s'] = int(idle_s - cur_asset[1])
            idle_asset['sub_idle_f'] = int(idle_f - cur_asset[2])

            all_data['idle_asset'] = idle_asset

            print(all_data)

            print(type(mem))
            print(type(acc_tot))
            print(type(mem_c_rate))
            print(type(idle_asset))
            print(type(all_data))

            return render(request, 'mypage/mypage.html', all_data)
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

        return redirect('mypageOpening')

