from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(AbstractUser):
    name = models.CharField(max_length = 30, unique = True, blank = False)
    description = models.CharField(max_length = 120, unique = False, blank = True)
    quantity = models.IntegerField(
    unique = False,
    validators = [MinValueValidator(0), MaxValueValidator(100)]
    )
