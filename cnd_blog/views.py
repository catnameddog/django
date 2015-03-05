import logging

from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView
from cnd_blog.models import Article

logger = logging.getLogger('django')

class ArticleYearArchiveView(YearArchiveView):
    date_field = 'pub_date'
    model = Article
    make_object_list = True

class ArticleMonthArchiveView(MonthArchiveView):
    date_field = 'pub_date'
    month_format = '%m'
    model = Article
    make_object_list = True

class ArticleDayArchiveView(DayArchiveView):
    date_field = 'pub_date'
    month_format = '%m'
    model = Article
    make_object_list = True
