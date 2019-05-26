from dataclasses import dataclass

from django.template.backends.django import Template
from django.template.loader import get_template

from .models import Task


def expand_tasks(tasks):
    tree = {}
    treenodes = []
    roots = []

    def add_to_tree(task):
        task_id = task.pk
        if task_id not in tree.keys():
            tasknode = TaskNode(node=task, id=task_id, children=[], expanded=task.expanded)
            tree[task_id] = tasknode
            treenodes.append(tasknode)
            return tasknode
        return tree[task_id]

    for task in tasks:
        parent = task.get_parent()
        if parent is None:
            root = add_to_tree(task)
            roots.append(root)
        else:
            parent_node = add_to_tree(parent)
            task_node = add_to_tree(task)
            parent_node.children.append(task_node)

    task_node: TaskNode
    for _, task_node in tree.items():
        task_node.childcount = len(task_node.children)

    return roots


@dataclass
class TaskNode:
    id: int
    children: list
    node: Task
    childcount = 0
    expanded: bool
