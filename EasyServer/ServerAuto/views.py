from django.http import HttpResponse
from django.shortcuts import render
from core import Controller


# Create your views here.
# index view
def index(request):
    return HttpResponse("works")
