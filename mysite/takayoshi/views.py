from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """index page"""
    return render(request,'index.html')


def qualities(request):
    """qualities page"""
    return render(request,'qualities.html')


def education(request):
    """education page"""
    return render(request,'education.html')


def experiences(request):
    """experiences page"""
    return render(request,'experiences.html')



def portfolio(request):
    """portfolio page"""
    return render(request,'portfolio.html')



