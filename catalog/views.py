from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Task, Worker, Position, TaskType


@login_required
def index(request):
    """View function for the home page of the site."""

    num_tasks = Task.objects.count()
    num_workers = Worker.objects.count()
    num_position = Position.objects.count()
    num_task_type = TaskType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_tasks": num_tasks,
        "num_workers": num_workers,
        "num_position": num_position,
        "num_task_type": num_task_type,
        "num_visits": num_visits + 1,
    }

    return render(request, "catalog/index.html", context=context)


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "tasktype_list"
    template_name = "catalog/tasktype_list.html"
    paginate_by = 5
