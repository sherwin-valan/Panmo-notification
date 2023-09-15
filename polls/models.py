from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Experiment(models.Model):
    name = models.CharField(max_length=100)
    checked = models.BooleanField(default=False)
    customer_email = models.EmailField()

    def __str__(self):
        return self.name
