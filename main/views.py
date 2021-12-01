from django.shortcuts import render
from django.utils import timezone
from . import models
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_items = models.Create.objects.all().order_by('-added_date')
    stuff_for_frontend = {
        'todo_items':todo_items
    }
    return render(request, 'main/item_list.html', stuff_for_frontend)

def add_item(request):
    item_name = request.POST['search']
    item_date = timezone.now()
    created_obj = models.Create.objects.create(text=item_name, added_date=item_date)
    return HttpResponseRedirect('/')

def delete_todo(request, todo_id):
    print(todo_id)
    models.Create.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')






