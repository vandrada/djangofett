from django.db import models
from django.db.models import DateTimeField
from django.utils import timezone
from django.contrib.auth.models import User as AuthUser
from taggit.managers import TaggableManager

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

    def inc(self):
        self.vote_count += 1
        self.save()

    def __str__(self):
        return "{}:{}".format(self.answer_text, self.vote_count)


class User(AuthUser):
    """
    Currently extends from auth.models.User
    Required fields are username, email, password
    """
    NOOB = 'NB'
    SAMARITAN = 'SM'
    PRO = 'PR'
    GOAT = 'GT'
    RANK_CHOICES = ((NOOB, "Noob"),
                    (SAMARITAN, "Samaritan"),
                    (PRO, "Professional"),
                    (GOAT, "Greatest of all time"))

    rank = models.CharField(max_length=2, choices=RANK_CHOICES, default=NOOB)

    def __str__(self):
        return self.username

    """
    Add up all the karma from the user's reviews.
    """
    def get_karma(self):
        return sum([rev.karma for rev in self.review_set.all()])

    """
    Get the user's report count from their reviews and comments
    """
    def get_report_count(self):
        report_count = 0
        report_count += sum([rev.reported_count
                             for rev in self.review_set.all()])
        report_count += sum([com.reported_count
                             for com in self.comment_set.all()])
        return report_count


class Game(models.Model):
    title = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    release_date = DateTimeField("Game's release date")
    tags = TaggableManager()
    image = models.ImageField(upload_to='games', null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=5000)    # is this long enough? yes
    author_id = models.ForeignKey(User)
    game_id = models.ForeignKey(Game)
    pub_date = DateTimeField()
    karma = models.IntegerField(default=0)
    reported_count = models.IntegerField(default=0)

    def inc_reports(self):
        self.reported_count += 1
        self.save()

    def preview(self):
        return self.body[:50] + "..."

    def __str__(self):
        return "{}... by {}".format(self.title[:10], self.author_id)


class Comment(models.Model):
    """
    Comments on reviews...and perhaps more.
    """
    body = models.CharField(max_length=1000)  # Same length as last.fm comments
    user_id = models.ForeignKey(User)
    review_id = models.ForeignKey(Review)
    timestamp = DateTimeField()
    reported_count = models.IntegerField(default=0)

    def __str__(self):
        return "{}... by {}".format(self.body[:10], self.user_id)
