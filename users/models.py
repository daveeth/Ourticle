from django.contrib.auth.models import AbstractUser
from django.db import models

class OurticleUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
