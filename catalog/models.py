from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("catalog:worker-detail", kwargs={"pk": self.pk})


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    deadline = models.DateTimeField(verbose_name="deadline", blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    URGENT = "URG"
    HIGH = "HI"
    MEDIUM = "MED"
    LOW = "LO"
    PRIORITY_CHOICES = (
        (URGENT, "Urgent"),
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low"),
    )
    priority = models.CharField(
        verbose_name="priority",
        max_length=3,
        choices=PRIORITY_CHOICES,
        default=MEDIUM,
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name="tasks")

    class Meta:
        ordering = ["deadline", "-priority"]

    def __str__(self):
        return f"{self.name} ({self.deadline} {self.task_type})"
