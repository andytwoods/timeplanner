from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel
from taggit.models import TagBase, GenericTaggedItemBase
from taggit_selectize.managers import TaggableManager
from tinymce.models import HTMLField


class Task(TimeStampedModel):

    labels = TaggableManager(blank=True)
    info = HTMLField("info", max_length=2000, blank=True)

    firstAncestor = models.ForeignKey("self", related_name='task_firstAncestor', blank=True, null=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey("self", related_name='task_parent', blank=True, null=True, on_delete=models.SET_NULL)

    complete = models.DateTimeField(default=None, blank=True)

    duration = models.TextField(null=True, default=None)

    priority = models.PositiveSmallIntegerField(default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)])
