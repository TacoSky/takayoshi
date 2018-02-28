from __future__ import unicode_literals
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64,primary_key=True)
    startdate = models.DateField()
    enddate = models.DateField()
    place = models.CharField(max_length=64)
    url = models.CharField(max_length=256,blank=True)
    description = models.CharField(max_length=1024)
    order = models.IntegerField(blank=True)

    def __str__(self):
        return u'%s' % (self.name)

'''Typo JobRole'''
class JobeRole(models.Model):
    name = models.CharField(max_length=64)
    company = models.ForeignKey('Company')
    startdate = models.DateField()
    enddate = models.DateField()
    description = models.CharField(max_length=1024)
    order = models.IntegerField(blank=True)

    def __str__(self):
        return u'%s' % (self.name)


class Experience(models.Model):
    name = models.CharField(max_length=64)
    role = models.ForeignKey('JobeRole')
    type = models.CharField(max_length=64)
    incharge = models.CharField(max_length=256,blank=True)
    achievement = models.CharField(max_length=256,blank=True)
    keyword = models.CharField(max_length=256,blank=True)
    url = models.CharField(max_length=256,blank=True)
    description = models.CharField(max_length=1024)
    order = models.IntegerField(blank=True)

    def __str__(self):
        return u'%s' % (self.name)







