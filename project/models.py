from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    
    def __str__(self):
        return self.title