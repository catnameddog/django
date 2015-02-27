import datetime

from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.utils.encoding import force_str, force_text

from cnd_blog.models import Post

import logging

logger = logging.getLogger('django')

class PostYearArchiveView(YearArchiveView):
    date_field = 'pub_date'
    queryset = Post.objects.all()
    make_object_list = True

def month_index(request, year, month):
    return HttpResponse("You're looking at entries for {year}-{month}".format(year=year, month=month))

def day_index(request, year, month, day):
    return HttpResponse("You're looking at entries for {year}-{month}-{day}".format(year=year, month=month, day=day))
