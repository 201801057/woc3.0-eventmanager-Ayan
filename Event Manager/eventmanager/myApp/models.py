from django.db import models
from django.contrib.auth.models import User
from password_generator import PasswordGenerator

import uuid
import random
import string
# Create your models here.

import string
import random


class EventRegistration(models.Model):
    eventId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    eventName = models.CharField(max_length=255)
    password = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=False)
    desc = models.CharField(max_length=255)
    posterLink = models.URLField()
    eventFrom = models.DateTimeField()
    eventTo = models.DateTimeField()
    eventDeadline = models.DateTimeField()
    hostID = models.EmailField()

    def __str__(self):
        return str(self.eventName)


class ParticipantRegistration(models.Model):
    pId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=12)
    emailID = models.EmailField()
    eventList = models.CharField(max_length=255)
    registrationType = models.CharField(max_length=255)
    noOfPeople = models.IntegerField()

    def __str__(self):
        return str(self.name)
