from django.http import JsonResponse
from django.shortcuts import render

from timeplanner.task.exceptions import MissingParentAndOrSiblingException
from .helpers import expand_tasks
from .models import Task


def get_parent_and_target_node(params):
    node_id = params.get('target')
    node: Task = Task.objects.get(id=node_id)
    parent_id = params.get('parent')
    parent_node: Task = Task.objects.get(id=parent_id)
    return parent_node, node

# Create your views here.
def run_command(command, params):

    if command == 'del':
        raise Exception('not implemented yet ' + command)

    if command == 'new':
        node_id = params.get('target')
        target_node: Task = Task.objects.get(id=node_id)
        sibling = target_node.add_sibling(pos='right')
        #sibling.title = '111'
        #sibling.save()

    elif command == 'text':
        node_id = params.get('target')
        val = params.get('val')
        target_node: Task = Task.objects.get(id=node_id)
        target_node.title = val
        target_node.save()

    elif command == 'move':
        node_id = params.get('target')
        direction = params.get('direction')
        raise Exception('not implemented yet ' + command)

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

    elif command == 'cursor_move':
        node_id = params.get('target')
        direction = params.get('direction')

        target_node: Task = Task.objects.get(id=node_id)
        parent_node = target_node.get_parent()
        if direction == '-1': # upward
            prev_sibling = target_node.get_prev_sibling()
            if prev_sibling is None:
                target_node.move(parent_node, 'last-child')
            else:
                target_node.move(prev_sibling, 'left')
        elif direction == '1': # downward
            next_sibling = target_node.get_next_sibling()
            if next_sibling is None:
                target_node.move(parent_node, 'first-child')
            else:
                target_node.move(next_sibling, 'right')
        else:
            raise Exception('unknown move direction: ' + direction)

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
