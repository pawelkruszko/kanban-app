from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def change_status(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.status == 'TODO':
        task.status = 'IN_PROGRESS'
    elif task.status == 'IN_PROGRESS':
        task.status = 'DONE'
    else:
        task.status = 'TODO'
    task.save()
    return redirect('task_list')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')
