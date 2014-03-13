from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdxpython.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # index page
    url(r'^$', 'apps.home.views.index', name='index'),
    url(r'^meetup_calendar$', 'apps.home.views.meetup_calendar', name='meetup_calendar'),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)
