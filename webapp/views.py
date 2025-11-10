from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task
from django.urls import reverse


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})


def create_task(request):
    if request.method == 'POST':
        description = request.POST['description']
        status = request.POST['status']
        deadline_date = request.POST['deadline_date']

        task = Task.objects.create(
            description=description,
            status=status,
            deadline_date=deadline_date
        )

        return redirect('task_detail', pk=task.pk)

    return render(request, 'create_task.html')
