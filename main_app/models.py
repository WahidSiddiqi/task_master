from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now

STATUS = (
    ('P', 'In Process'),
    ('H', 'On Hold'),
    ('C', 'Completed')
)
DEPARTMENT = (
    ('Quality/Testing'),
    ('Developers'),
    ('Design'),
    ('Arquitect'),
    ('Manager'),
)

# Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

# Comment
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

# Project
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    