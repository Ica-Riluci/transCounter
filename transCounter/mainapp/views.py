from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import *

# Create your views here.
global nouser
global wrongpw

nouser = False
wrongpw = False

@login_required
def index(request):
    # logout(request)
    return HttpResponse('Hello, world. You\'re at the mainapp\'s index.')

def login_check(request):
    global nouser
    global wrongpw
    if request.method == 'GET':
        return HttpResponseRedirect('/main/login')
    else:
        nouser = False
        wrongpw = False
        f = LoginForm(request.POST)
        if f.is_valid():
            try:
                usr = User.objects.get(username=request.POST['username'])
                lusr = authenticate(request, username=request.POST['username'], password=request.POST['password'])
                if lusr is not None:
                    login(request, lusr)
                    return HttpResponseRedirect('/main/')
                else:
                    wrongpw = True
                    return HttpResponseRedirect('/main/login/')
            except User.DoesNotExist:
                nouser = True
                return HttpResponseRedirect('/main/login/')

def loginp(request):
    global nouser
    global wrongpw
    f = LoginForm()
    context= {
        'form' : f,
        'nouser' : nouser,
        'wrongpw' : wrongpw
    }
    return render(request, 'mainapp/login.html', context)