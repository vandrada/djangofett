from django.db import models
from django.db.models import DateTimeField
import datetime
from django.utils import timezone

"""
'models.py', by Everyone
Define models for djangofett website
"""


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = DateTimeField("Time of poll creation")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Answer(models.Model):
    answer_text = models.CharField(max_length=50, default="")
    question = models.ForeignKey(Question)
    vote_count = models.IntegerField(default=0)
