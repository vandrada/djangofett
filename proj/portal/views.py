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


def review(request, review_id):
    context = {'review': Review.objects.get(id=review_id)}
    return render(request, 'portal/review.html', context)
    pass


def user():
    # TODO
    pass


def vote(request, question_id):
    context = {'question': Question.objects.get(id=question_id)}
    return render(request, 'portal/vote.html', context)

#######################
########## USER CONTROL

##### Register User
def userctrl_doreg(request):
   if request.method == 'POST':
      username = request.POST['reg_un']
      email = request.POST['reg_email']
      password = request.POST['reg_pw']

      if User.objects.filter(username=username).count():
         loginResult = "Username already Exists"
      else:
         # Save new User
         from django.contrib.auth.models import User
         newUser = User.objects.create_user(username, email, password)
         newUser.save()
         
         # Attempt Authenticate the User
         from django.contrib.auth import authenticate, login
         loggedInUser = authenticate(username=username, password=password)

      # Did it work?
      if loggedInUser is not None:
         if loggedInUser.is_active:
            # Yes, log them in.
            login(request, loggedInUser)
            loginResult = 0
         else:
            # No, their account is inactive.
            loginResult = 1
      else:
         # No, something is wrong!  HALP!
         loginResult = 2

      return render(request, 'userctrl/registration_result.html', {'login_result':loginResult})
   