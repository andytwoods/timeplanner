from django.urls import path
from . import views

urlpatterns = [
    path("schedule/", view=views.home, name="schedule"),

    path('schedule/<int:id>/json/', views.CalendarJsonListView.as_view(), name='calendar_json'),
    path('schedule/json/', views.CalendarJsonListView.as_view(), name='calendar_json_all'),
]
