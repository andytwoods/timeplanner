from django.http import JsonResponse
from django.shortcuts import render

from timeplanner.task.exceptions import MissingParentAndOrSiblingException
from .helpers import expand_tasks
from .models import Task


def get_parent_and_node(params):
    node_id = params.get('target')
    node: Task = Task.objects.get(id=node_id)


# Create your views here.
def run_command(command, params):

    if command == 'del':
        raise Exception('not implemented yet')

    elif command == 'left':
        raise Exception('not implemented yet')
        parent, node = get_parent_and_node(params)

    elif command == 'right':
        raise Exception('not implemented yet')

    elif command == 'up':
        raise Exception('not implemented yet')

    elif command == 'down':
        raise Exception('not implemented yet')

    elif command == 'text':
        node_id = params.get('target')
        val = params.get('val')
        target_node: Task = Task.objects.get(id=node_id)
        target_node.title = val
        target_node.save()

    elif command == 'move':
        node_id = params.get('target')
        direction = params.get('direction')
        print(node_id, direction)
        raise Exception('not implemented yet')
    elif command == 'update':
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
            target_node: Task = Task.get_first_root_node()
            moved_node.move(target_node, pos='left')

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
