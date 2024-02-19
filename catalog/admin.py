from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from catalog.models import (
    TaskType,
    Position,
    Worker,
    Task,
)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "position",
                )
            },
        ),
    )


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "deadline",
        "is_completed",
        "priority",
        "task_type",
    ]
    list_filter = ["deadline"]
    search_fields = ["name"]
