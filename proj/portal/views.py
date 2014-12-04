from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from portal.models import Game, Question, Review, Answer, PollResponse, User
from portal.models import ReviewResponse, Comment
from portal.forms import ReviewForm, CommentForm, UserForm
import random
import datetime
from django.utils import timezone
from django.http import HttpResponseRedirect
from collections import namedtuple
import sys


# Create your views here.
def game(request, game_id):
    game = Game.objects.get(id=game_id)
    context = {'game': game}
    return render(request, 'portal/games.html', context)


def home(request):
    rand = random.randint(1, len(Question.objects.all()))
    random_question = Question.objects.get(id=rand)
    recent_reviews = Review.objects.all().order_by('-pub_date')[:10]
    #recent_reviews = Review.objects.filter(pub_date__lt=timezone.now() -
    #                                        datetime.timedelta(days=1))
    context = {'question': random_question, 'reviews': recent_reviews}
    return render(request, 'portal/home.html', context)

#Deprecated? I'm keeping it here just in case.
"""
def review(request, review_id):
    review = Review.objects.get(id=review_id)
    comment_list = Comment.objects.all().filter(review_id=review).order_by('-timestamp')
    print(comment_list) #Just a debug statement..
    context = {'review': Review.objects.get(id=review_id),
                'comments': comment_list}
    return render(request, 'portal/review.html', context)
"""

def review_report(request, review_id):
    review = Review.objects.get(id=review_id)
    msg = False
    form = CommentForm()
    comment_list = Comment.objects.all().filter(review_id=review).order_by('-timestamp')
    #Prevent multiple downvotes & anonymous voting
    if (request.user.__str__() != "AnonymousUser"):
        if ReviewResponse.objects.all().filter(review=review, user=request.user).count() == 0:
                review.inc_reports()
                r = ReviewResponse(review=review, user=request.user)
                r.save()
        else:
            msg = "An upvote/report from this user has already been submitted.\n"
    else:
        msg = "Please log in to upvote/report.\n"
    context = {'review': Review.objects.get(id=review_id), 
            'msg' : msg, 'form': form, 'comments': comment_list}
    #return redirect('/djangofett/review/{}'.format(review_id))
    return render(request, 'portal/review_comment.html', context)


def review_karma(request, review_id):
    review = Review.objects.get(id=review_id)
    msg = False
    form = CommentForm()
    comment_list = Comment.objects.all().filter(review_id=review).order_by('-timestamp')
    #Prevent multiple upvotes & anonymous voting
    if (request.user.__str__() != "AnonymousUser"):
        if ReviewResponse.objects.all().filter(review=review, user=request.user).count() == 0:
            review.inc_karma()
            r = ReviewResponse(review=review, user=request.user)
            r.save()
        else:
            msg = "An upvote/report from this user has already been submitted.\n"
    else:
        msg = "Please log in to upvote/report.\n"
    context = {'review': Review.objects.get(id=review_id),
               'msg' : msg, 'form': form, 'comments': comment_list}
    return render(request, 'portal/review_comment.html', context)

#Allows a user to write comments on review pages.
def review(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if request.user.__str__() != "AnonymousUser":
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user_id = request.user
                comment.review_id = Review.objects.get(id=review_id)
                comment.timestamp = timezone.now() #Gives weird time.
                comment.save()
        return HttpResponseRedirect('/djangofett/review/{}'.format(review_id))
    else:
        form = CommentForm()
        comment_list = Comment.objects.all().filter(review_id=review).order_by('-timestamp')
        return render(request, 'portal/review_comment.html', {
            'form' : form, 'review' : review, 'comments': comment_list})
        

def review_create(request, game_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.pub_date = timezone.now()
            review.author_id = request.user
            review.game_id = Game.objects.get(id=game_id)
            review.save()
            return HttpResponseRedirect('/djangofett/review/{}'.format(review.id))
    #else:
    form = ReviewForm()
    return render(request, 'portal/review_edit.html', {
        'form' : form,
    })

def review_edit(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            #Save the data in the database as a Review object.
            review = form.save(commit=False)
            review.pub_date = timezone.now()
            review.save()
            return HttpResponseRedirect('/djangofett/review/{}'.format(review.id))
    #Create an empty form if 'GET' was used instead. Prevent unauthorized
    #review modifications.
    elif request.user == review.author_id:
        form = ReviewForm(instance=review)
        return render(request, 'portal/review_edit.html', {
            'review': review,
            'form' : form,
        })
    else:
        return home(request) #Placeholder: tell the usr they can't do this.

def user(request, user_id):
    print("Within user")
    u = User.objects.get(id=user_id)
    rank = dict(u.RANK_CHOICES).get(u.assert_rank())
    context = {'karma': u.get_karma(),
               'rank': rank,
               'about': u.about}
    return render(request, 'portal/user.html', context)

#Allow the user to edit their about me via the edit button.
def edit_about(request, user_id):
    u = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=u)
        if form.is_valid():
            usr = form.save(commit=False)
            usr.about = u.about
            usr.save()
            return HttpResponseRedirect('/djangofett/user/{}'.format(user_id))
            #render(request, 'portal/user.html', context)
    #If the form isn't valid or if the method isn't post, falling through
    #to this block is sufficient.
    form = UserForm()
    rank = dict(u.RANK_CHOICES).get(u.assert_rank())
    context = {'karma': u.get_karma(),
               'rank': rank,
               'form': form, 
               'about': u.about}
    return render(request, 'portal/edit_about.html', context)

def vote(request, question_id, answer_id):
    question = Question.objects.get(id=question_id)
    msg = False #Utilize for convenient error msging.
    answer = get_object_or_404(Answer, pk=answer_id)
    if (request.user.__str__() != "AnonymousUser"):
        if PollResponse.objects.all().filter(question=question, user=request.user).count() == 0:
            answer.inc()
            p = PollResponse(question=question, user=request.user)
            p.save()
            #PollResponse.objects.create(question=question, user=request.user)
            print("Voted")
        else: 
            msg = "A vote from this user has already been registered."
    else: 
        msg = "Please log in to vote."
    # calculate the highest after the model has been updated
    highest = question.answer_set.order_by('vote_count').reverse()[0]
    rest = question.answer_set.order_by('vote_count').reverse()[1:]
    context = {'question': question, 'highest': highest, 'rest': rest, 'msg': msg}
    return render(request, 'portal/vote.html', context)


def result(request, question_id):
    """
    Just the results...no votes
    """
    question = Question.objects.get(id=question_id)
    highest = question.answer_set.order_by('vote_count').reverse()[0]
    rest = question.answer_set.order_by('vote_count').reverse()[1:]
    context = {'question': question, 'highest': highest, 'rest': rest}
    return render(request, 'portal/result.html', context)

#-------------------------------------
#-------- GAME LIST/SEARCH RESULT VIEW
def game_list(request, platform_id):
   context = {}
   results = {}
   # Search only comes from POST requests
   if request.method == 'POST':
      meta_mode = 1
      query = request.POST['search_query']
      query = query.strip()

      if query == "":
         meta_mode = 2
      else:
         tokens = query.split()
         tags = {tag.strip("#") for tag in tokens if tag.startswith("#")}

         results = Game.objects.all().order_by('-release_date')
         for tag in tags:
            results = results.filter(tags__name__in=[tag])
         for t in tokens:
            if not t.startswith("#"):
               results = results.filter(title__contains=t)

         context['query'] = query

   # Clicked a Navbar Item
   else:
      meta_mode = 0
      results = Game.objects.filter(tags__name__in=[platform_id]).order_by('-release_date')

   for game in results:
      game.review_count = Review.objects.filter(game_id=game.id).count()

   context['game_list'] = results
   context['meta_mode'] = meta_mode
   context['meta_platform'] = platform_id
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
         regResult = 1
         msg = "That username is already in use. Please choose another."
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
               regResult = 0
               msg = str(r"Registration successful!  You have been logged in."+
                          "Redirecting to home page...")
            else:
               # No, their account is inactive.
               regResult = 2
               msg = str(r"Sorry, something went wrong during"+
                        "registration. =(  Please try again...")
                        
         else:
            # No, something is wrong!  HALP!
            regResult = 2
            msg = str(r"Sorry, something went wrong during"+
                        "registration. =(  Please try again...")

      context = {'reg_result' : regResult, 'msg' : msg}
      return render(request, 'userctrl/logreg_result.html', context)

#---- User Log In
def userctrl_login(request):
   if request.method == 'POST':
      username = request.POST['login_un']
      password = request.POST['login_pw']

      user = authenticate(username=username, password=password)
      if user is not None:
         if user.is_active:
            login(request, user)
            #user(request, user)
            return redirect(request.META['HTTP_REFERER'])
            #return redirect('/djangofett/user/'+str(user.id))
         else:
            msg = "Sorry, but your account is disabled."
            regResult = 1
            context = {'reg_result' : regResult, 'msg' : msg}
            return render(request, 'userctrl/logreg_result.html',context)
      # Return a 'disabled account' error message CHECK
      else:
         msg = str(r"Either the password or username you entered was invalid."+
                " Please try again.")
         regResult = 1
         context = {'reg_result' : regResult, 'msg' : msg}
         return render(request, 'userctrl/logreg_result.html',context)
      # Return an 'invalid login' error message. CHECK

#---- User Log Out
def userctrl_logout(request):
   logout(request)
   return redirect('/djangofett/')


#----- END USER CONTROL VIEWS
#----------------------------
