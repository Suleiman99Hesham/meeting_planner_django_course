from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def welcome(request):
    return HttpResponse("<html> <head>Meeting planner</head> <body><h1>Welcome to the meeting planner</h1> </body></html>")


def date(request):
    return HttpResponse("this page was served at "+str(datetime.now()))


def about(request):
    return HttpResponse("my name is suleiman, i'm django developer, i love python")