from django.db import models

# Create your models here.

class ImageGallery(models.Model):
    file_name = models.CharField(max_length=128)
    file_title = models.CharField(max_length=256)
    caption = models.TextField(max_length=1000, blank=True)
    sort_order = models.IntegerField()
    show_in_set = models.BooleanField(default=True)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):              # __unicode__ on Python 2
        return self.file_title
