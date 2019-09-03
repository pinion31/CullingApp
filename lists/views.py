from django.shortcuts import render, redirect
from lists.models import List, Item

# Create your views here.
def user_lists(request):
  if request.method == 'POST':
    List.objects.create(name=request.POST['list_name'])
    return redirect('/user-list')
  list_all = List.objects.all()
  return render(request, 'user_list.html', {'list_all': list_all})
