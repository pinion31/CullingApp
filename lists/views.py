from django.shortcuts import render

# Create your views here.
def create_lists(request):
  return render(request, 'create_list.html')
