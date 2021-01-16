from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome to the meeting planner!")

def date(request):
    return HttpResponse("This page is server at " +str(datetime.now()))

def aboutme(request):
    return HttpResponse("This is about me")



