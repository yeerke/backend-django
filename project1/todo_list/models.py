from platform import mac_ver
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    users = models.

    # owner add later
    # mark add later
