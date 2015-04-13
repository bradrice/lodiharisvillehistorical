from django.contrib import admin
from .models import ImageGallery

# Register your models here.


class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('file_title', 'file_name')


admin.site.register(ImageGallery, ImageGalleryAdmin)