# -*- coding: utf-8 -*-
import json
from django.db.models.query import QuerySet

from timeplanner.task.models import Task


def event_queryset_serializer(tasks, match_user=None):
    objects_body = []

    for task in tasks:
        field = event_serializer(task)
        objects_body.append(field)

    return json.dumps(objects_body)


IS_PARTICIPANT_CLASS = 'bg-warning'
PARTICIPANT_ALLOCATED_CLASS = 'bg-secondary text-white'
GENERAL_BOOKING_CLASS = 'bg-primary text-white'
NO_PARTICIPANT_ALLOCATED_CLASS = 'bg-light'
SELECTABLE = 'selectable'

TITLE_FREE = 'free'
TITLE_TAKEN = 'taken'

IS_PARTICIPANT = 'is-participant'


def event_serializer(task: Task):

    return {
        "id": task.pk,
        "startEditable": True,
        "title": task.title,
        "className": IS_PARTICIPANT_CLASS,
        "start": task.start_iso,
        "end": task.end_iso,
    }
