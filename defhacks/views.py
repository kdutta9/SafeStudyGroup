from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def wall():
    return HttpResponse("Logged in.")

def signup(request):
    return render(request, 'signup.html')
