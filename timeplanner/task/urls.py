from django.urls import path
from . import views


app_name = "task"
urlpatterns = [
    path("tasks/", view=views.home, name="list"),
]
