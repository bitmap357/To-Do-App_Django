from django.db import models

# Create your models here.
class Task(models.Model):
    
    d
    name = models.CharField(max_length=100)
    priority = models.IntegerField()