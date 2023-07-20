from django.db import models
from project.models import Project

class New(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
