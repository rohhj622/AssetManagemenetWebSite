from django.shortcuts import render

# Create your views here.
def mypage(request):
    return render(request, 'main_page/main.html')
