""" Views image """
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from images.forms import ImageCreateForm
from images.models import Image


@login_required
def image_create(request):
    """ View image created """
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html',
                  {'section': 'image', 'form': form})


def image_detail(request, id_image, slug):
    """ View detail image """
    image = get_object_or_404(Image, id=id_image, slug=slug)
    return render(request, 'images/image/detail.html',
                  {'section': 'images', 'image': image})
