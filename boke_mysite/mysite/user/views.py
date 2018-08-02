from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def index(request):
    return render(request,'message/lw-index.html')
def no(request):
    return render(request, 'message/no.html')
def sign_in(request):
    return render(request,'message/sign_in.html')
def sign_up(request):
    return render(request,'message/sign_up.html')

def login1(request):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)

            return HttpResponse('登陆成功')
        else:

            return HttpResponse('账号未激活')

    else:
        return HttpResponse('用户不存在')

def register(request):
    username=request.POST['username']
    password=request.POST['password']

    user=User.objects.create_user(username=username,password=password)
    if user is not None:
        return redirect('sign_up')
    else:
        pass




