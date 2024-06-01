from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task

def addTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    context = {'form':form}
    return render(request, 'task/add_task.html', context)


def updateTask(request, id):
    task = Task.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'task/add_task.html', context)


def deleteTask(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('home')