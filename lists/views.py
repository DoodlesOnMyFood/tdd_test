from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request,'lists/home.html')

def view_list(request, list_id):
    correct_list = List.objects.get(id=list_id)
    if request.method == 'POST':
        Item.objects.create(list=correct_list,text=request.POST['item_text'])
        return redirect(f'/lists/{list_id}/')
    return render(request, 'lists/list.html', {'list':correct_list})

def new_list(request):
    new_list = List.objects.create()
    item = Item(text=request.POST['item_text'],list=new_list)
    try:
        item.full_clean()
        item.save()
    except:
        new_list.delete()
        error = 'You can\'t have an empty list item'
        return render(request, 'lists/home.html', {'error':error})
    return redirect(f'/lists/{new_list.id}/')

