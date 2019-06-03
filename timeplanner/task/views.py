from django.http import JsonResponse
from django.shortcuts import render

from timeplanner.task.exceptions import MissingParentAndOrSiblingException
from .helpers import expand_tasks
from .models import Task


# Create your views here.
def run_command(command, params):
    print(params)
    if command == 'update':
        node_id = params.get('target')
        node_parent = params.get('parent', None)
        node_prev_sibling = params.get('prev_sibling', None)

        moved_node: Task = Task.objects.get(id=node_id)

        if node_prev_sibling:
            target_node: Task = Task.objects.get(id=node_prev_sibling)
            moved_node.move(target_node, pos='right')
        elif node_parent:
            target_node: Task = Task.objects.get(id=node_parent)
            moved_node.move(target_node, pos='first-child')
        else:
            raise MissingParentAndOrSiblingException(str(params))

    return JsonResponse({'success': True})


def home(request):
    
    command = request.GET.get('command', None)
    if command is not None:
        return run_command(command, request.GET)

    tasks = Task.ordered_tasks()
    expanded_tasks = expand_tasks(tasks)

    context = {
        'expanded_tasks': expanded_tasks
    }
    return render(request, 'task/tasks_home.html', context)
