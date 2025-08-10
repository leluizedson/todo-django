from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def list_tasks(request):
    tasks = Task.objects.all()

    return render(request, 'tasks/list_tasks.html', {'tasks': tasks})

def ver_task(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'tasks/ver_task.html', {'task':task})

def create_task(request):
    request.method == 'POST'
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list_tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')
        else:
            form = TaskForm(instance=task)
        return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('list_tasks')
    return render(request, 'tasks/delete_task.html', {'task': task})