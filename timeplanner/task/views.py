from django.shortcuts import render

from .helpers import expand_tasks
from .models import Task

# Create your views here.
def home(request):

    tasks = Task.ordered_tasks()
    expanded_tasks = expand_tasks(tasks)

    context = {
        'expanded_tasks': expanded_tasks
    }
    return render(request, 'task/tasks_home.html', context)
