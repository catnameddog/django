import datetime

from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render

def year_index(request, year):
    return HttpResponse("You're looking at entries for {year}".format(year=year))

def month_index(request, year, month):
    return HttpResponse("You're looking at entries for {year}-{month}".format(year=year, month=month))

def day_index(request, year, month, day):
    return HttpResponse("You're looking at entries for {year}-{month}-{day}".format(year=year, month=month, day=day))
