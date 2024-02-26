from django.urls import path

from .views import (
    index,
    TaskListView,
    TaskTypeListView,
    WorkerListView,
    PositionListView,
    TaskCreateView,
    WorkerCreateView,
    TaskTypeCreateView,
    PositionCreateView,
    TaskDetailView,
    WorkerDetailView,
    TaskUpdateView,
    TaskDeleteView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    PositionUpdateView,
    PositionDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasktypes/", TaskTypeListView.as_view(), name="tasktype-list"),
    path("tasktypes/create/", TaskTypeCreateView.as_view(), name="tasktype-create"),
    path("tasktypes/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="tasktype-update"),
    path("tasktypes/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="tasktype-delete"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),

]

app_name = "catalog"
