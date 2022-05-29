from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .models import Post 
from django.contrib.auth.models import User, auth
from django.contrib import messages



def index(request):
    return render(request, 'index.html')

def lc(request):
    if request.method=="POST":
        from main import ml_code as ml
        
    return render(request, 'lc.html')



def lp(request):
    return render(request, 'lp.html')

def ls(request):
    return render(request, 'ls.html')

def pp(request):
    ''' This is for the attendance view'''
    return render(request, 'attendance.csv')


def loginPage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        # print(username)
        # print(password)
        user=auth.authenticate(username=username, password=password)
        # print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return render(request, 'login2.html') 

        
        
    else:
        return render(request, 'login2.html')

