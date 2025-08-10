from django.shortcuts import render, get_object_or_404
from . models import Task
from django.shortcuts import HttpResponse

def list_tasks(request):
    tasks = Task.objects.all()

    return render(request, 'list_tasks.html', {'tasks': tasks})

def ver_task(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'task/ver_task.html', {'task':task})