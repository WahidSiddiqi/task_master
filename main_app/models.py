from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now

STATUS = (
    ('P', 'In Process'),
    ('H', 'On Hold'),
    ('C', 'Completed')
)

# Comment
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

# Project
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

# #Tasks
# class Tasks(model.Model):
#     class Status(models.TextChoices):
#         PENDING = 'Pending'
#         IN_PROGRESS = 'InProgress'
#         COMPLETED = 'Completed'
#         ON_HOLD = 'OnHold'

# class Priority(models.TextChoices):
#     HIGH = 'High'
#     MEDIUM ='Medium'
#     LOW = 'Low'

#     title = models.CharField(max_length=100)
#     description = model.CharField(max_length=250)
#     status = models.CharField(max_length=10 choices=Status.choices, defualt=Status.PENDING)
#     created_by = models.ForeignKey(User, related_name='owned_tasks', on_delete=mondels.CASCADE)
#     owner = models.ForeignKey(User, related_name='owned_tasks', on_delete=models.CASCADE)
#     created_date = models.DateTimeField(auto_now_add=TRUE)
#     comment = models.TextField(null=TRUE, blank=TRUE)
#     project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE, null=True, blank=True)
#     priority = models.CharField(max_length=6, choices=Priority.choices, defult=Priority.MEDIUM)

# def__str__(self):
#     return self.title
    