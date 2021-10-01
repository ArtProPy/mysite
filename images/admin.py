""" Images on admin site """
from django.contrib import admin

from images.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """ Images on admin site """
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']
