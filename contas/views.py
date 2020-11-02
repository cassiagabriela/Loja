from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('user')
        password = request.POST.get('senha')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuario e senha inválidos, tente novamente')
    return redirect('/login/')


