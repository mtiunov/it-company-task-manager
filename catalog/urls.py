from django.urls import path

from .views import (
    index,
    TaskListView,
    TaskTypeListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasktypes/", TaskTypeListView.as_view(), name="tasktype-list"),

]

app_name = "catalog"
