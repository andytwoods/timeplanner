from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel
from taggit.models import TagBase, GenericTaggedItemBase
from taggit_selectize.managers import TaggableManager
from tinymce.models import HTMLField
from treebeard.mp_tree import MP_Node


class Task(TimeStampedModel, MP_Node):

    ROOT_USERNAME = 'my_root'

    labels = TaggableManager(blank=True)
    title = models.TextField()
    info = HTMLField("info", max_length=2000, blank=True)

    complete = models.DateTimeField(blank=True, null=True)

    duration = models.TextField(null=True, default=None)

    priority = models.PositiveSmallIntegerField(default=1, validators=[
            MaxValueValidator(3),
            MinValueValidator(1)])

    expanded = models.BooleanField(default=True)

    # move: https://django-treebeard.readthedocs.io/en/latest/api.html#treebeard.models.Node.move
    @classmethod
    def ordered_tasks(cls):

        tasks = list(Task.objects.all()) #filter(expanded=True))

        tree = {}

        task: Task
        for task in tasks:
            pass

        return tasks




