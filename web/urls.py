from django.conf.urls import *
import os
from .views import Index, gallery, History, Pictures, Business, Cemetery, Railroad

urlpatterns = patterns('',
url(r'^$', Index.as_view(), name='index'),
url(r'^gallery', gallery, name='gallery'),
url(r'^history$', History.as_view(), name='history'),
url(r'^pictures$', Pictures.as_view(), name='pictures'),
url(r'^pictures/business', Business.as_view(), name='business'),
url(r'^pictures/cemetery', Cemetery.as_view(), name='cemetery'),
url(r'^pictures/railroad', Railroad.as_view(), name='railroad'),
)