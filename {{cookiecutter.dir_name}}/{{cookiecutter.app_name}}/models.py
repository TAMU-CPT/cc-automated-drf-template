from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import uuid

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)

class Iteration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course)
    users = models.ManyToManyField(User)
    start_date = models.DateField()
    end_date = models.DateField()

class Assessment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    iteration = models.ForeignKey(Iteration)
    start_date = models.DateField()
    end_date = models.DateField()

class Result(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User)
    assessment = models.ForeignKey(Assessment)
    submitted = models.DateTimeField(blank=True, null=True)
    score = models.FloatField()
