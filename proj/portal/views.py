from django.shortcuts import render
from portal.models import Game, Question, Review
import random
import datetime
from django.utils import timezone


# Create your views here.
def game(request, game_id):
    game = Game.objects.get(id=game_id)
    context = {'game': game}
    return render(request, 'portal/games.html', context)


def home(request):
    rand = random.randint(1, len(Question.objects.all()))
    random_question = Question.objects.get(id=rand)
    recent_reviews = Review.objects.filter(pub_date__lt=timezone.now() -
                                           datetime.timedelta(days=1))
    context = {'question': random_question, 'reviews': recent_reviews}
    return render(request, 'portal/home.html', context)


def review():
    # TODO
    pass


def user():
    # TODO
    pass


def vote(request, question_id):
    context = {'question': Question.objects.get(id=question_id)}
    return render(request, 'portal/vote.html', context)
