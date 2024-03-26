from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.models.CharField(_(""), max_length=50)