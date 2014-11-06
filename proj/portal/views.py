from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from portal.models import Game, Question, Review, Answer
import random
import datetime
from django.utils import timezone
from collections import namedtuple

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


def review_report(request, review_id):
    review = Review.objects.get(id=review_id)
    review.inc_reports()
    context = {'review': Review.objects.get(id=review_id)}
    return render(request, 'portal/review_report.html', context)


def user():
    # TODO
    pass


def vote(request, question_id, answer_id):
    answer = Answer.objects.get(id=answer_id)
    answer.inc()
    context = {'question': Question.objects.get(id=question_id)}
    return render(request, 'portal/vote.html', context)


def result(request, question_id):
    """
    Just the results...no votes
    """
    context = {'question': Question.objects.get(id=question_id)}
    return render(request, 'portal/result.html', context)

#-------------------------------------
#-------- GAME LIST/SEARCH RESULT VIEW
def game_list(request, platform_id):
   context = {}
   # Search only comes from POST requests
   if request.method == 'POST':
      meta_mode = 1
      print("----- searching...")
      query = request.POST['search_query']
      query = query.strip()
      
      if query == "":
         print("Empty query!")
         meta_mode = 2
      else:
         tokens = query.split()
         tags = {tag.strip("#") for tag in tokens if tag.startswith("#")}
         
         print("-- Query: ")
         print(tokens)
         print("-- tags:")
         print(tags)
         results = Game.objects.all().order_by('-release_date')
         for tag in tags:
            results = results.filter(tags__name__in=[tag])
         for t in tokens:
            if not t.startswith("#"):
               results = results.filter(title__contains=t)
   
   # Clicked a Navbar Item
   else:
      meta_mode = 0
      print("----- "+platform_id+" games:")
      results = Game.objects.filter(tags__name__in=[platform_id]).order_by('-release_date')
      
      for game in results:
         game.review_count = Review.objects.filter(game_id=game.id).count()
      
      print(results)
      
   context = { 'game_list': results, 'meta_mode':meta_mode, 'meta_platform':platform_id }
   return render(request, 'gamelist.html', context)
#---- END GAME LIST/SEARCH RESULT VIEW
#-------------------------------------

#----------------------------
#--------- USER CONTROL VIEWS
#---- Register User
def userctrl_doreg(request):
   if request.method == 'POST':
      username = request.POST['reg_un']
      email = request.POST['reg_email']
      password = request.POST['reg_pw']

      # Is this username valid?
      if User.objects.filter(username=username).count():
         # No
         regResult = "Username already Exists"
      else:
         # Yes, save the new user account.
         newUser = User.objects.create_user(username, email, password)
         newUser.save()
         
         # Attempt Authenticate the User
         loggedInUser = authenticate(username=username, password=password)

         # Did it work?
         if loggedInUser is not None:
            if loggedInUser.is_active:
               # Yes, log them in.
               login(request, loggedInUser)
               regResult = "Registration successful.  You have been logged in."
            else:
               # No, their account is inactive.
               regResult = "Registration Failed =(.  Account is disabled."
         else:
            # No, something is wrong!  HALP!
            regResult = "Registration Failed =(.  A total meltdown occured somewhere.  Please try again later."

      return render(request, 'userctrl/registration_result.html', {'reg_result':regResult, 'request':request})

#---- User Log In
def userctrl_login(request):
   if request.method == 'POST':
      username = request.POST['login_un']
      password = request.POST['login_pw']

      user = authenticate(username=username, password=password)
      if user is not None:
         if user.is_active:
            login(request, user)
            return redirect('/fettdb/placeholder')
         #else:
      # Return a 'disabled account' error message
      else:
         return redirect('/fettdb/placeholder')
      # Return an 'invalid login' error message.

#---- User Log Out
def userctrl_logout(request):
   logout(request)
   return redirect('/fettdb/placeholder')


#----- END USER CONTROL VIEWS
#----------------------------
