# -*- coding: utf-8 -*-
from config.views import User
import json
from django.db.models.query import QuerySet

from study.models import LabSession, BOOKING_TYPE_GENERAL


def event_queryset_serializer(events, show_name, match_user=None):
    objects_body = []

    if isinstance(events, QuerySet):
        for event in events:
            field = event_serializer(event, show_name, match_user)
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


def event_serializer(lab_session: LabSession, is_experimenter: bool, match_user: User = None):

    if is_experimenter:
        if lab_session.participant is not None:
            class_name = PARTICIPANT_ALLOCATED_CLASS
            title = lab_session.participant.user.username
        elif lab_session.type == BOOKING_TYPE_GENERAL:
            class_name = GENERAL_BOOKING_CLASS + " " + SELECTABLE
            title = 'General booking (' + str(lab_session.created_by) + ')'
        else:
            class_name = NO_PARTICIPANT_ALLOCATED_CLASS + " " + SELECTABLE
            title = 'free'

    else:  # is participant
        if lab_session.participant is not None:
            if lab_session.participant.user == match_user:
                class_name = IS_PARTICIPANT_CLASS + " " + SELECTABLE + " " + IS_PARTICIPANT
                title = match_user.username
            else:
                class_name = PARTICIPANT_ALLOCATED_CLASS
                title = TITLE_TAKEN
        else:
            title = TITLE_FREE
            class_name = NO_PARTICIPANT_ALLOCATED_CLASS + " " + SELECTABLE

    if lab_session.room_id is not None:
        title = str(lab_session.room_id) + ': ' + title

    return {
        "id": lab_session.pk,
        "startEditable": is_experimenter,
        "title": title,
        "className": class_name,
        "start": lab_session.start_iso,
        "end": lab_session.end_iso,
    }
