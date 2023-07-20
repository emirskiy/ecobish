from django.db import models
from project.models import Project

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    def __str__(self):
        return self.name