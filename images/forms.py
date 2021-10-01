""" Images forms """
from urllib import request

from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from images.models import Image


class ImageCreateForm(forms.ModelForm):
    """Form by create image"""

    def clean_url(self):
        """ Checking the image extension """
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not '\
                                        'match valid image extensions.')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        """ Save form image """
        image = super(ImageCreateForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = f"{slugify(image.title)}.{image_url.rsplit('.', 1)[1].lower()}"
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image.save()
        return image

    class Meta:
        """Meta by form image"""
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {'url': forms.HiddenInput}
