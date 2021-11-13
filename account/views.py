import re
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def signin(request):
    return render(request,'account/login.html')

def register(request):
    return render(request,'account/register.html')

def reguser(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(Q(email=email) or Q(username=username)).exists():
            return HttpResponse("Account Already Exist")
        else:
            newuser = User.objects.create_user(username,email,password)
            newuser.save()
            return HttpResponse('Account Created Successfully. Please Login')

def loginuser(request):
    username = request.POST['username']
    password = request.POST['password']
    username.lower()
    if User.objects.filter(username=username).exists():
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return redirect('login')

def log_out(request):
    logout(request)
    return redirect('/login')