from django.http import JsonResponse
from django.shortcuts import render

from .helpers import expand_tasks
from .models import Task

# Create your views here.
def run_command(command):
    print(command)
    return JsonResponse({})


def home(request):
    
    command = request.GET.get('command', None)
    if command is not None:
        return run_command(command)

    tasks = Task.ordered_tasks()
    expanded_tasks = expand_tasks(tasks)

    context = {
        'expanded_tasks': expanded_tasks
    }
    return render(request, 'task/tasks_home.html', context)
