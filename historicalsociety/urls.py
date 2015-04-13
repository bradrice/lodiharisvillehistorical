from django.conf.urls import patterns, include, url
from django.contrib import admin
import os
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Home.as_view()', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^web/', include('web.urls', namespace='web')),
    url(r'^$', RedirectView.as_view(url='web/', permanent=False)),
        )


