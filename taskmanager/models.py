import datetime
from django.db import models
from django.utils import timezone

class Subject(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Task(models.Model):

    class StatutEnum(models.TextChoices):
        PENDING = "PENDING", "Pending"
        COMPLETED = "COMPLETED", "Completed"
        STARTED = "STARTED", "Started"

    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    deadline = models.DateTimeField("Deadline", null = True, blank=True)
    status = models.CharField( max_length= 10,
                            choices = StatutEnum.choices,
                            default= StatutEnum.PENDING,
    )
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def describe(self):
        return self.description

    def is_recent(self):
        return self.created_at >= timezone.now()-datetime.timedelta(days=1)
