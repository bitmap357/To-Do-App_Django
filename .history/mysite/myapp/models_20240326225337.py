from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(_("") max_length=50)