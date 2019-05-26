from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import Task


class TaskAdmin(TreeAdmin):
    form = movenodeform_factory(Task)


admin.site.register(Task, TaskAdmin)
from django.contrib import admin

# Register your models here.
