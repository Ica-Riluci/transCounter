from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.

def index(request):
    return HttpResponse('Hello, world. You\'re at the mainapp\'s index.')

def login(request):
    if request.method == 'GET':
        f = LoginForm()
        context= {
            'form' : f
        }
        return render(request, 'mainapp/login.html', context)
    else:
        f = LoginForm(request.POST)
        if f.is_valid():
            return HttpResponseRedirect('/main/')