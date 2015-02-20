from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
import os


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Home.as_view()', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.Index.as_view(), name='home'),
)
