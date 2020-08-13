from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List
from django.core.exceptions import ValidationError
from lists.forms import ItemForm
from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request,'lists/home.html', {'form': ItemForm()})

def view_list(request, list_id):
    correct_list = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save(for_list=correct_list)
            return redirect(correct_list)

    return render(request, 'lists/list.html', {'form':form, 'list':correct_list})

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'lists/home.html', {"form":form})
