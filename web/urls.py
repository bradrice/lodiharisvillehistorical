from django.conf.urls import *
import os
from .views import Index, gallery, History

urlpatterns = patterns('',
url(r'^$', Index.as_view(), name='index'),
url(r'^gallery', gallery, name='gallery'),
url(r'^history$', History.as_view(), name='history'),
)