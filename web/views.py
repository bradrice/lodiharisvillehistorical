from django.shortcuts import render

# Create your views here.

class Index(TemplateView):
    template_name = "index.html"


def gallery(request):
    dir_name = 'images/home_gallery'
    directorypath = os.path.join(settings.MEDIA_ROOT, dir_name)
    img_list =os.listdir(directorypath)
    return render_to_response('gallery.html', {'images': img_list})