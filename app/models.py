from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(required=False)
    status = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, related_name="tasks")
