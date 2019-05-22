from django.shortcuts import render, get_object_or_404
from applications.example_task.models import Task


def index(request):
    # Get objects from database
    tasks = Task.objects.all()

    context = {
        'tasks': tasks,
    }

    return render(request, 'pages/index.html', context)
