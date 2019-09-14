from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.


def create_user(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            request.POST['username'], request.POST['email'], request.POST['password'])
        user.save()
        return redirect('/home')
    return render(request, 'auth_users/create_user.html')


def login_user(request):
    return render(request, 'auth_users/login.html')
