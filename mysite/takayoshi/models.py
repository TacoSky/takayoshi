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
        return u'%s' % self.name


class JobeRole(models.Model):
    name = models.CharField(max_length=64)
    company = models.ForeignKey('Company')
    startdate = models.DateField()
    enddate = models.DateField()
    description = models.CharField(max_length=1024)
    order = models.IntegerField(blank=True)

    def __str__(self):
        return u'%s' % self.name


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
        return u'%s' % self.name

    def keywords(self):
        return self.keyword.split(",").extend(self.incharge.split(","))


class Classification(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64)

    def __str__(self):
        return u'%s' % self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=64)
    company = models.ForeignKey('Company')
    achievement = models.CharField(max_length=256,blank=True)
    order = models.IntegerField(blank=True)
    image = models.CharField(max_length=256)
    url = models.CharField(max_length=256,blank=True)
    description = models.CharField(max_length=1024,blank=True)

    def __str__(self):
        return u'%s' % self.name







