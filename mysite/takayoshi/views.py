from django.shortcuts import render
from django.http import HttpResponse
from .models import Classification, Experience, JobeRole, Company, Portfolio

# Create your views here.


class CtnExps:
    def __init__(self, arvexp, arvkey):
        self.exp = arvexp
        self.key = arvkey


class CtnRoles:
    def __init__(self, arvrole, arvexps):
        self.role = arvrole
        self.exps = arvexps


class CtnCompanies:
    def __init__(self, arvcomp, arvroles):
        self.comp = arvcomp
        self.roles = arvroles


class CtnKeyword:
    def __init__(self, keyword, experience, classific):
        self.key = keyword
        self.exp = experience
        self.cls = classific



def index(request):
    """index page"""
    return render(request,'index.html')


def qualities(request):
    keywords = []

    tempexps = Experience.objects.all().order_by('order')
    cl = Classification.objects.all()
    for exp in tempexps:
        if exp.keyword != "":
            for key in exp.keyword.split(","):
                flag = False
                for valu in keywords:
                    if key == valu.key:
                        valu.exp = valu.exp + 1
                        flag = True
                if flag is False:
                    keywords.append(CtnKeyword(key, 1, cl.filter(name=key)[0].type))

        if exp.incharge != "":
            for crg in exp.incharge.split(","):
                flag = False
                for valu in keywords:
                    if crg == valu.key:
                        valu.exp = valu.exp + 1
                        flag = True
                if flag is False:
                    keywords.append(CtnKeyword(crg, 1, cl.filter(name=crg)[0].type))

    data = {
        'keywords': sorted(sorted(keywords, key=lambda t: t.key), key=lambda t: t.exp, reverse=True),
    }
    """qualities page"""
    return render(request,'qualities.html', data)



def education(request):
    datacomps = []

    """get experiences"""
    companies = Company.objects.all().order_by('order')
    for comp in companies:

        temproles = []
        joberoles = JobeRole.objects.all().filter(company=comp).order_by('order')
        for role in joberoles:
            tempexps = Experience.objects.all().filter(role=role).filter(type="Student").order_by('order')
            expctns = []
            for exp in tempexps:
                expctns.append(CtnExps(exp, exp.keywords()))
            if expctns.__len__() != 0:
                temproles.append(CtnRoles(role, expctns))
        if temproles.__len__() != 0:
            datacomps.append(CtnCompanies(comp, temproles))

    data = {
        'companies': datacomps,
    }

    """education page"""
    return render(request,'education.html',data)


def experiences(request):
    datacomps = []

    """get experiences"""
    companies = Company.objects.all().order_by('order')
    cl = Classification.objects.all()
    for comp in companies:

        temproles = []
        joberoles = JobeRole.objects.all().filter(company=comp).order_by('order')
        for role in joberoles:
            tempexps = Experience.objects.all().filter(role=role).exclude(type="Student").order_by('order')
            expctns = []
            for exp in tempexps:
                keywords = []
                for key in exp.keywords():
                    if key != "":
                        keywords.append(CtnKeyword(key, 1, cl.filter(name=key)[0].type))
                expctns.append(CtnExps(exp, sorted(keywords, key=lambda t: t.cls)))
            if expctns.__len__() != 0:
                temproles.append(CtnRoles(role, expctns))
        if temproles.__len__() != 0:
            datacomps.append(CtnCompanies(comp, temproles))

    data = {
        'companies': datacomps,
    }

    """experiences page"""
    return render(request,'experiences.html', data)



def portfolio(request):
    portfolios = Portfolio.objects.all().order_by('order')

    data = {
        'portfolios': portfolios,
    }
    return render(request,'portfolio.html', data)



