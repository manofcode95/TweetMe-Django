from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
User=get_user_model()
def user_login(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
    return render (request, 'login.html', {'form':form})


def user_register(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(username)
        user=User.objects.create_user(username=username, email=email, password=password)
        return redirect('/')
    return render(request, 'register.html', {'form':form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')