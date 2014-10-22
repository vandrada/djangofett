from django.db import models
from django.db.models import DateTimeField
from django.utils import timezone
from django.contrib.auth.models import User as AuthUser

import datetime

"""
'models.py', by Everyone
Define models for djangofett website
"""


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = DateTimeField("Time of poll creation")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    answer_text = models.CharField(max_length=50, default="")
    question = models.ForeignKey(Question)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return "{}:{}".format(self.answer_text, self.vote_count)


class User(AuthUser):
    """
    Currently extends from auth.models.User
    Required fields are username, email, password
    """
    karma = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Game(models.Model):
    title = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    release_date = DateTimeField("Game's release date")

    def __str__(self):
        return self.title
