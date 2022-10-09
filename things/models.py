from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Thing(AbstractUser):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 120)
    quantity = models.CharField(max_length = 3)
