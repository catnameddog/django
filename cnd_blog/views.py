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

class PostMonthArchiveView(YearArchiveView):
    date_field = 'pub_date'
    queryset = Post.objects.all()
    make_object_list = True

class PostDayArchiveView(YearArchiveView):
    date_field = 'pub_date'
    queryset = Post.objects.all()
    make_object_list = True
