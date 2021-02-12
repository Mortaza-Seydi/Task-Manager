from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status_choices = (
        ('T', 'To Do'),
        ('D', 'Doing'),
        ('I', 'In Test'),
        ('O', 'Done'),
        ('B', 'Blocked')
    )
    status = models.CharField(max_length=1, choices=status_choices)
    start_time = models.DateField(blank=True)
    end_time = models.DateField(blank=True)


class Board(models.Model):
    members = models.ManyToManyField(User, through='Project')


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    details = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ForeignKey(Board, on_delete=models.CASCADE)
    task = models.ManyToManyField(Task, blank=True)
