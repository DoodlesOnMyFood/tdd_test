from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request,'lists/home.html')

def view_list(request, list_id):
    correct_list = List.objects.get(id=list_id)
    return render(request, 'lists/list.html', {'list':correct_list})

def new_list(request):
    new_list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=new_list)
    return redirect(f'/lists/{new_list.id}/')

def add_item(request, list_id):
    the_list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=the_list)
    return redirect(f'/lists/{list_id}/')
