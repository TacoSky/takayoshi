from django.shortcuts import render
from django.http import HttpResponse
from .models import Company, JobeRole, Experience

# Create your views here.

class CtnRoles:
    def __init__(self, arvrole, arvexps):
        self.role = arvrole
        self.exps = arvexps


class CtnCompanies:
    def __init__(self, arvcomp, arvroles):
        self.comp = arvcomp
        self.roles = arvroles



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
    datacomps = []

    """get experiences"""
    companies = Company.objects.all().order_by('order')
    for comp in companies:

        temproles = []
        joberoles = JobeRole.objects.all().filter(company=comp).order_by('order')
        for role in joberoles:
            tempexps = Experience.objects.all().filter(role=role).order_by('order')
            temproles.append(CtnRoles(role, tempexps))
        datacomps.append(CtnCompanies(comp, temproles))

    data = {
        'companies': datacomps,
    }

    """experiences page"""
    return render(request,'experiences.html', data)



def portfolio(request):
    """portfolio page"""
    return render(request,'portfolio.html')



