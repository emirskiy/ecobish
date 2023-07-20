from django.db import models
from project.models import Project

class Event(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
