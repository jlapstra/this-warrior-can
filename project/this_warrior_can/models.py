from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date


class User(AbstractUser):
    """
        https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractuser
    """
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    sober_date = models.DateField(null=True, blank=True)


class TimeSober(models.Model):
    """
        A way to keep track of how long its been since you did a bad habbit
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, blank=True)
    sober_date = models.DateField(null=True, blank=True)

    def get_time_sober(self):
        today = date.today()
        return (today - self.sober_date).days

