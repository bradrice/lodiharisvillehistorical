from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import ImageGallery
import os
from django.conf import settings
from django.shortcuts import render_to_response
from django.http.response import HttpResponse

# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'
    model = ImageGallery

    def dispatch(self, *args, **kwargs):
        return super(Index, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        return ImageGallery.objects.get(show_in_set=True)

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['images'] = ImageGallery.objects.filter(show_in_set=True).order_by('sort_order')
        return context


def gallery(request):
    dir_name = 'images/home_gallery'
    directorypath = os.path.join(settings.MEDIA_ROOT, dir_name)
    img_list =os.listdir(directorypath)
    return render_to_response('gallery.html', {'images': img_list})

class History(TemplateView):
    template_name = 'history.html'

    def dispatch(self, *args, **kwargs):
        return super(History, self).dispatch(*args, **kwargs)