from django.shortcuts import render
from webapp.models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})


def create_task(request):
    created_task = None
    if request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        deadline_date = request.POST.get('deadline_date') or None

        created_task = Task.objects.create(
            description=description,
            status=status,
            deadline_date=deadline_date
        )

    return render(request, 'tasks/create_task.html', {'created_task': created_task})


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    tasks = Task.objects.all().order_by('id')
    return render(request, 'tasks/index.html', {'tasks': tasks})