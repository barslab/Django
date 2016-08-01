from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    group_number = models.TextField()
    user = models.ForeignKey(User, unique=True)
    # def __str__(self):
    #     return self.user