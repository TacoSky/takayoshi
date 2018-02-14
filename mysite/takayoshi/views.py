from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """index page"""
    return render(request,'index.html')


