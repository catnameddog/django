import datetime

from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.utils.encoding import force_str, force_text

from cnd_blog.models import Article

import logging

logger = logging.getLogger('django')

class ArticleYearArchiveView(YearArchiveView):
    date_field = 'pub_date'
    queryset = Article.objects.all()
    make_object_list = True

class ArticleMonthArchiveView(YearArchiveView):
    date_field = 'pub_date'
    queryset = Article.objects.all()
    make_object_list = True

class ArticleDayArchiveView(YearArchiveView):
    date_field = 'pub_date'
    queryset = Article.objects.all()
    make_object_list = True
