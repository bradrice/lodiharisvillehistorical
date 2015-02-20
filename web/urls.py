from django.conf.urls import *
import os
from .views import Index,

url(r'^$', Index.as_view(), name='index'),
