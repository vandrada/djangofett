from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
   return HttpResponse("Hello World!!")

def base(request):
   return render(request, 'base.html')

def gamelist(request):
   return render(request, 'gamelist.html')

def placeholder(request):
   return render(request, 'placeholder.html', {'request':request})