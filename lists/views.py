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
    error = None
    if request.method == 'POST':
        try: 
            item = Item(list=correct_list,text=request.POST['text'])
            item.full_clean()
            item.save()
            return redirect(correct_list)
        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, 'lists/list.html', {'list':correct_list, 'error':error})

def new_list(request):
    new_list = List.objects.create()
    item = Item(text=request.POST['text'],list=new_list)
    try:
        item.full_clean()
        item.save()
    except:
        new_list.delete()
        error = 'You can\'t have an empty list item'
        return render(request, 'lists/home.html', {'error':error})
    return redirect(new_list)

