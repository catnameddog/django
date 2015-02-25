from django.conf.urls import patterns, url

from cnd_blog import views

urlpatterns = patterns('',
#        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^(?P<year>\d{4})/$', views.year_index, name='year_index'),
        url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.month_index, name='month_index'),
        url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', views.day_index, name='day_index'),
        )

