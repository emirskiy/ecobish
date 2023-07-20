from django.db import models
from project.models import Project

class NatureHelp(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title