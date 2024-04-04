from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
user = get_user_model()


class Profile(models.Model):
    author = models.OneToOneField(user, on_delete=models.CASCADE)
    bio = models.TextField(default='', blank=True)