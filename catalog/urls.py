from django.urls import path

from .views import (
    index,
    TaskListView,
    TaskTypeListView,
    WorkerListView,
    PositionListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasktypes/", TaskTypeListView.as_view(), name="tasktype-list"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("positions/", PositionListView.as_view(), name="position-list"),

]

app_name = "catalog"
