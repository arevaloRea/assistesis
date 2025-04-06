from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_status2 = models.BooleanField(default=False)
    is_status3 = models.BooleanField(default=False)

