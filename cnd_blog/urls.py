from django.conf.urls import patterns, url
from django.views.generic.dates import ArchiveIndexView

from cnd_blog import views
from cnd_blog.views import ArticleYearArchiveView, ArticleMonthArchiveView, ArticleDayArchiveView
from cnd_blog.models import Article

urlpatterns = patterns('',
        url(r'^archive/$', 
            ArchiveIndexView.as_view(model=Article, date_field="pub_date", queryset=Article.objects.all()), 
            name='archive'), 
        url(r'^(?P<year>\d{4})/$',
            ArticleYearArchiveView.as_view(),
            name='article_year_archive'),
        url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
            ArticleMonthArchiveView.as_view(),
            name='article_month_archive'),
        url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
            ArticleDayArchiveView.as_view(),
            name='article_day_archive'),
        )

