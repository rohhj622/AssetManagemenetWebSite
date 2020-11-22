from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def expirationDateOpen(request):
    return render(request, 'expiration_date/cal_expiration_assets.html')
