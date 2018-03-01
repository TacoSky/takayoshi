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

class CtnKeyword:
    def __init__(self, keyword, experience):
        self.key = keyword
        self.exp = experience

class CtnCnCharge:
    def __init__(self, incharge, experience):
        self.inc = incharge
        self.exp = experience


def index(request):
    """index page"""
    return render(request,'index.html')


def qualities(request):
    KasMarketer = []
    KasEngineer = []
    KasCreator  = []
    CasMarketer = []
    CasEngineer = []
    CasCreator  = []

    tempexps = Experience.objects.all().order_by('order')
    for exp in tempexps:
        for key in exp.keyword.split(","):
            if exp.type == u'Marketer':
                flag = False
                for valu in KasMarketer:
                    if key == valu.key:
                        valu.exp = valu.exp + 1
                        flag = True
                if flag is False:
                    KasMarketer.append(CtnKeyword(key, 1))

            if exp.type == u'Engineer':
                flag = False
                for valu in KasEngineer:
                    if key == valu.key:
                        valu.exp = valu.exp + 1
                        flag = True
                if flag is False:
                    KasEngineer.append(CtnKeyword(key, 1))

            if exp.type == u'Creator':
                flag = False
                for valu in KasCreator:
                    if key == valu.key:
                        valu.exp = valu.exp + 1
                        flag = True
                if flag is False:
                    KasCreator.append(CtnKeyword(key, 1))

        for crg in exp.incharge.split(","):
            if crg == u'':
                '''nothing to do'''
            elif exp.type == u'Marketer':
                flag = False
                for valu in CasMarketer:
                    if crg == valu.inc:
                        valu.exp = valu.exp + 1
                        flag = True
                if flag is False:
                    CasMarketer.append(CtnCnCharge(crg, 1))

            elif exp.type == u'Engineer':
                flag = False
                for valu in CasEngineer:
                    if crg == valu.inc:
                        valu.exp = valu.exp + 1
                        flag = True
                if flag is False:
                    CasEngineer.append(CtnCnCharge(crg, 1))

            elif exp.type == u'Creator':
                flag = False
                for valu in CasCreator:
                    if crg == valu.inc:
                        valu.exp = valu.exp + 1
                        flag = True
                if flag is False:
                    CasCreator.append(CtnCnCharge(crg, 1))

    data = {
        'KasMarketer': sorted(KasMarketer, key=lambda t: t.exp, reverse=True),
        'KasEngineer':  sorted(KasEngineer, key=lambda t: t.exp, reverse=True),
        'KasCreator': sorted(KasCreator, key=lambda t: t.exp, reverse=True),
        'CasMarketer':  sorted(CasMarketer, key=lambda t: t.exp, reverse=True),
        'CasEngineer': sorted(CasEngineer, key=lambda t: t.exp, reverse=True),
        'CasCreator':  sorted(CasCreator, key=lambda t: t.exp, reverse=True),
    }
    """qualities page"""
    return render(request,'qualities.html', data)


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



