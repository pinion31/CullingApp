from django.shortcuts import render, redirect
from lists.models import List, Item
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def user_lists(request):
    print(request.GET.get('index'))
    open_list = request.GET.get('index') or False
    if request.method == 'POST':
        List.objects.create(name=request.POST['list_name'])
        return redirect('/user-list')
    list_all = List.objects.all()
    print(open_list)
    return render(request, 'lists/user_list.html', {'list_all': list_all, 'open_list': open_list})

