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
    template_name = 'timeline.html'

    def dispatch(self, *args, **kwargs):
        return super(History, self).dispatch(*args, **kwargs)


class Pictures(TemplateView):
    template_name = 'pictures.html'

    def dispatch(self, *args, **kwargs):
        return super(Pictures, self).dispatch(*args, **kwargs)


def myfiles_page(request):
    article_dict = {'Scan-034.jpg':'Larry Scott/School','Scan-027.jpg':'Train Depot (part 2)','Scan-041.jpg':'Joe Warner/First article','Scan-151.jpg':'Lodi Library','Scan-030.jpg':'Bentons Store','Scan-001.jpg':'Dr. Crum House','Scan-009.jpg':'Dr. Joseph Harris House (part 1)','Scan-028.jpg':'Benson Family','Scan-038.jpg':'American Legion','Scan-026.jpg':'Train Depot 9 (part 1)','Scan-045.jpg':'Indian Gets make over (part 1)','Scan-022.jpg':'Train Depot Awarded','Scan-053.jpg':'The Snell Family','Scan-029.jpg':'The Scott Family','Scan-044.jpg':'The Lodi Indian','Scan-006.jpg':'Grover Rice House','Scan-007.jpg':'Alloy Fabricators Donate Plagues','Scan-010.jpg':'Joseph Harris House (part 2)','Scan-021.jpg':'Caboose to get Facelift','Scan-046.jpg':'Indian Makeover (part 2)','Scan-054.jpg':'Lomer Griffin','Scan-016.jpg':'Hower-Homan House','Scan-002.jpg':'Joseph Warren House Organizations','Scan-033.jpg':'School Stories','Scan-018.jpg':'The Mong House','Scan-017.jpg':'The Billman House','Scan-040.jpg':'Woodlawn Cemetery','Scan-037.jpg':'Garden Isle/Hall Farm','Scan-035.jpg':'Doctors','Scan-015.jpg':'Timothy Burr House','Scan-048.jpg':'Dick Anderson','Scan-050.jpg':'The Big Truck','Scan-056.jpg':'Baker-Grannis House','Scan-014.jpg':'Amasa Clapp House','Scan-020.jpg':'Lodi Lumber Celebrates 125 years','Scan-150.jpg':'Cloverleaf art School Helps LHHS','Scan-043.jpg':'Lodi Log Cabin','Scan-011.jpg':'Victorian Xmas Characters','Scan-005.jpg':'Waite-Harris House','Scan-013.jpg':'Ye Olde Tyme Christmas','Scan-047.jpg':'Eli Beachy/Alloy','Scan-032.jpg':'Post Office','Scan-042.jpg':'George Gould','Scan-003.jpg':'Congregational Church','Scan-052.jpg':'Taylor Inn','Scan-004.jpg':'George Burr House','Scan-012.jpg':'Christmas with a Historical Twist','Scan-024.jpg':'Grimm Boys','Scan-019.jpg':'Tulips by Larry','Scan-039.jpg':'Howers Store','Scan-025.jpg':'Fire Department','Scan-008.jpg':'Higbee/Crum House','Scan-036.jpg':'Lodi Hospital','Scan-023.jpg':'Lodi Alumni gather'}
    dir_name = 'docs/tparticles'
    directorypath = os.path.join(settings.MEDIA_ROOT, dir_name)
    doclist = os.listdir(directorypath)
    for i in doclist:
        print(article_dict.get(i))

    return render_to_response('tradingpost.html', {'data' : article_dict})