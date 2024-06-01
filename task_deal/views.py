from django.shortcuts import render
from task.models import Task

def home(request):
    data = Task.objects.all()    
    context= {'tasks': data}
    return render(request, 'home.html', context)