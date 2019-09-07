import datetime

import pytz
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from config import settings
from timeplanner.schedule.serializers import event_queryset_serializer
from timeplanner.schedule.utils import timestamp_to_datetime


def home(request):
    return None



@method_decorator(login_required, name='dispatch')
class CalendarJsonListView(ListView):
    template_name = 'study/schedule_events.html'

    def get_queryset(self):
        # todo: select related
        study_id = self.kwargs.get('id', None)

        if study_id:
            study = Study.objects.select_related('researcher__user').get(id=self.kwargs.get('id'))
            is_researcher = study.researcher.user == self.request.user if study else True
            is_researcher = False

            if is_researcher:
                queryset = LabSession.objects.filter(room_in=study.room_choice)
            else:
                queryset = LabSession.objects.filter(study=study)
        else:
            queryset = LabSession.objects.all()
            is_researcher = True
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

        if is_researcher is False:
            queryset = queryset.filter(
                Q(date__gte=datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE))) |
                Q(participant__user=self.request.user)
            )

        return event_queryset_serializer(queryset, is_researcher, self.request.user)
