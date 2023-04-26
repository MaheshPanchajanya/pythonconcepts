from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

from django.http import HttpRequest
from django.contrib import messages

from teracota.models import Ads

#from .models import Byusr
from django.contrib.auth.models import User, auth


def login(request):
    asadregim = Ads.objects.all()
    return render(request,"login_pottery.html",{'asadregim':asadregim})


def logout(request):
    auth.logout(request)
    return redirect('/')








       
