from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.


def create_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/home')
    else:
        form = UserRegisterForm()
    return render(request, 'auth_users/create_user.html', {'form': form})


def login_user(request):
    return render(request, 'auth_users/login.html')
