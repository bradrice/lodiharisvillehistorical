from django.conf.urls import *
import os
from .views import Index, gallery, myfiles_page, History, Pictures
from django.views.generic import TemplateView

urlpatterns = patterns('',
url(r'^$', Index.as_view(), name='index'),
url(r'^gallery', gallery, name='gallery'),
url(r'^tradingpost', myfiles_page, name='tradingpost'),
url(r'^timeline$', TemplateView.as_view(template_name="timeline.html"), name='timeline'),
url(r'^history$', TemplateView.as_view(template_name="history.html"), name='history'),
url(r'^pictures$', Pictures.as_view(), name='pictures'),
url(r'^pictures/business', TemplateView.as_view(template_name='business.html'), name='business'),
url(r'^pictures/cemetery', TemplateView.as_view(template_name='cemetery.html'), name='cemetery'),
url(r'^pictures/railroad', TemplateView.as_view(template_name='railroad.html'), name='railroad'),
url(r'^/test$', TemplateView.as_view(template_name='test.html'), name='test'),
url(r'^member$', TemplateView.as_view(template_name='member.html'), name='test'),
)