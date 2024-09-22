from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home(request):
    return HttpResponse("home",content_type="application/json")

def about(request):
    return HttpResponse("About",content_type="application/json")