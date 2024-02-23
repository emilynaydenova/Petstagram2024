from django.shortcuts import render, redirect, get_object_or_404

from photos.forms import PhotoForm, PhotoEditForm
from photos.models import Photo


# Create your views here.
def add_photo(request):
    form = PhotoForm(request.POST or None, request.FILES)
    if form.is_valid():
        photo = form.save()
        return redirect('photo_details', pk=photo.pk)

    context = {
        'form': form,
    }

    return render(request, "photos/photo-add-page.html", context)


def photo_details(request, pk):
    context = {
        'photo': Photo.objects.get(pk=pk),
    }
    return render(request, "photos/photo-details-page.html", context)


def photo_edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    if request.method == 'POST':
        form = PhotoEditForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()

            return redirect('photo_details', pk)
    else:
        form = PhotoEditForm(instance=photo)

    context = {
        'photo': photo,
        'form': form,
    }
    return render(request, "photos/photo-edit-page.html", context)


def photo_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    return redirect('home')
