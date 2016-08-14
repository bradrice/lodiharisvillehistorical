from django.conf.urls import patterns, include, url
from django.contrib import admin
import os
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse

from historicalsociety import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Home.as_view()', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^blog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^web/', include('web.urls', namespace='web')),
    url(r'^$', RedirectView.as_view(url='web/', permanent=False)),
    url(r'^ckeditor/', include('ckeditor.urls')),
        )


