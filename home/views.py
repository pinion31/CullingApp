from django.shortcuts import render

# Create your views here.


def dashboard(request):
    create_list = False
    return render(request, 'home/home.html', {'create_list': create_list})
