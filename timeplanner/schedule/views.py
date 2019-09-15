import datetime

import pytz
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from config import settings
from timeplanner.schedule.serializers import event_queryset_serializer
from timeplanner.schedule.utils import timestamp_to_datetime
from timeplanner.task.models import Task


def home(request):
    return None



class CalendarJsonListView(ListView):
    template_name = 'schedule/schedule.html'

    def get_queryset(self):
        # todo: select related
        study_id = self.kwargs.get('labels', None)

        if study_id:
            label_tags = list(Task.labels.names())

            job_tags_len = 100 / len(label_tags)

            queryset = Task.objects.filter(labels__name__in=label_tags) \
                .prefetch_related('tags') \
                .annotate(overlap=Count('id') * job_tags_len) \
                .order_by('-overlap', 'id').distinct()

        else:
            queryset = Task.objects.all()

        _timezone = self.request.GET.get('timezone')
        from_str = self.request.GET.get('start', False)
        to_str = self.request.GET.get('end', False)

        if from_str:
            from_date = datetime.datetime.fromisoformat(from_str)
            from_date = from_date.replace(tzinfo=pytz.timezone(_timezone))
        else:
            from_date = None

        if to_str:
            to_date = datetime.datetime.fromisoformat(to_str)
            to_date = to_date.replace(tzinfo=pytz.timezone(_timezone))
        else:
            to_date = None

        if from_date and to_date:
            queryset = queryset.filter(
                date__range=(
                    from_date + datetime.timedelta(-30),
                    to_date
                )
            )
        elif from_date:
            queryset = queryset.filter(
                date__gte=timestamp_to_datetime(from_date)
            )
        elif to_date:
            queryset = queryset.filter(
                date__lte=timestamp_to_datetime(to_date)
            )

        return event_queryset_serializer(queryset, self.request.user)
