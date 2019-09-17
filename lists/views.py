from django.shortcuts import render, redirect
from .models import List, Item
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
# Create your views here.

# class UserNoteListView(LoginRequiredMixin, ListView):
#     model = List
#     template_name = 'lists/user_list.html'
#     context_object_name = 'list_all'
    
    # def test_func(self):
    #     list = self.get_object()
    #     return self.request.user == list.author

# class ListDetailView(LoginRequiredMixin, DetailView):
#     model = List
#     template_name = 'lists/list_details.html'

@login_required
def list_items(request, pk):
    selected_list = List.objects.get(pk=pk)
    if request.method == 'POST':
        Item.objects.create(content=request.POST.get('list_item'), list_parent_id=pk)
        return redirect(f"/list/{pk}/")
    all_items = Item.objects.filter(list_parent_id=pk)
    return render(request, 'lists/list_items.html', {'all_items': all_items, 'list':selected_list})

@login_required
def user_lists(request):
    open_list = request.GET.get('index') or False
    if request.method == 'POST':
        List.objects.create(name=request.POST['list_name'])
        return redirect('/user-list')
    list_all = List.objects.all()
    return render(request, 'lists/user_list.html', {'list_all': list_all, 'open_list': open_list})

