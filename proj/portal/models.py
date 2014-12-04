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

#WIP: Log user's responses to polls.
class PollResponse(models.Model):
    question = models.ForeignKey('Question')
    user = models.ForeignKey('auth.User')

#Log user's responses to reviews (karma votes/reports)
class ReviewResponse(models.Model):
    review = models.ForeignKey('Review')
    user = models.ForeignKey('auth.User')

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = DateTimeField("Time of poll creation")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class User(AuthUser):
    """
    Currently extends from auth.models.User
    Required fields are username, email, password
    TODO: Define method to discern class based on karma count.
    """
    NOOB = 'NB'
    SAMARITAN = 'SM'
    PRO = 'PR'
    GOAT = 'GT'
    RANK_CHOICES = ((NOOB, "Noob"),
                    (SAMARITAN, "Samaritan"),
                    (PRO, "Professional"),
                    (GOAT, "Greatest of all time"))
    #max_length for rank changed to 30 to allow full names to display.
    rank = models.CharField(max_length=30, choices=RANK_CHOICES, default=NOOB)
    about = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to="games/", null=True)

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
    """
    Discern the user's rank.
    """
    def assert_rank(self):
        karma = self.get_karma()
        if karma < 10:
            self.rank = self.NOOB
        elif karma < 20:
            self.rank = self.SAMARITAN
        elif karma < 30:
            self.rank = self.PRO
        else:
            self.rank = self.GOAT
        return self.rank

class Answer(models.Model):
    answer_text = models.CharField(max_length=50, default="")
    question = models.ForeignKey(Question)
    vote_count = models.IntegerField(default=0)

    def inc(self):
        self.vote_count += 1
        print(type(self.vote_count))
        self.save()

    def __str__(self):
        return "{}:{}".format(self.answer_text, self.vote_count)


    
class Game(models.Model):
    title = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    release_date = DateTimeField("Game's release date")
    tags = TaggableManager()
    image = models.ImageField(upload_to='games', null=True)

    def __str__(self):
        return self.title
     
    def get_absolute_url(self):
       return "/djangofett/game/%i/" % self.id


class Review(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField() 
    author_id = models.ForeignKey('auth.User')
    game_id = models.ForeignKey('Game')
    pub_date = DateTimeField(default=timezone.now)
    karma = models.IntegerField(default=0)
    reported_count = models.IntegerField(default=0)

    def inc_reports(self):
        self.reported_count += 1
        self.save()

    def inc_karma(self):
        self.karma += 1
        self.save()

    def preview(self):
        return self.body[:50] + "..."

    def __str__(self):
        return "{}... by {}".format(self.title[:10], self.author_id)


class Comment(models.Model):
    """
    Comments on reviews...and perhaps more.
    """
    body = models.TextField(max_length=1000)  # Same length as last.fm comments
    user_id = models.ForeignKey('auth.User')
    review_id = models.ForeignKey(Review)
    timestamp = DateTimeField(default=timezone.now)
    reported_count = models.IntegerField(default=0)
    #NOTE: Probably unnecessary.
    def __str__(self):
        return "{}... by {}".format(self.body[:10], self.user_id)
