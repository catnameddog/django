from django.conf.urls import patterns, url
from django.views.generic.dates import ArchiveIndexView

from cnd_blog import views
from cnd_blog.views import PostYearArchiveView, PostMonthArchiveView, PostDayArchiveView
from cnd_blog.models import Post

urlpatterns = patterns('',
        url(r'^archive/$', 
            ArchiveIndexView.as_view(model=Post, date_field="pub_date", queryset=Post.objects.all()), 
            name='archive'), 
        url(r'^(?P<year>\d{4})/$',
            PostYearArchiveView.as_view(),
            name='post_year_archive'),
        url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
            PostMonthArchiveView.as_view(),
            name='post_month_archive'),
        url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
            PostDayArchiveView.as_view(),
            name='post_day_archive'),
        )

