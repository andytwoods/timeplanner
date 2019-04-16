from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    context = {
        'expanded_tasks': Task.objects.filter(expanded=True)
    }
    return render(request, 'task/tasks_home.html', context)
