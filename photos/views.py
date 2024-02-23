from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from common.forms import CommentForm
from photos.forms import PhotoForm, PhotoEditForm
from photos.models import Photo
from django.views import generic as views


# Create your views here.

class CreatePhotoView(views.CreateView):
    form_class = PhotoForm
    template_name = "photos/photo-add-page.html"  # default is "pets/pet_form.html
    context_object_name = "pet"

    def get_success_url(self):
        return reverse_lazy("photo_details", kwargs={
            'pk': self.object.pk
        })


class PhotoDetailsView(views.DetailView):
    queryset = Photo.objects.all() \
        .prefetch_related("comment_set") \
        .prefetch_related("like_set") \

    template_name = "photos/photo-details-page.html"
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['comment_form'] = CommentForm()
        return context


class PhotoEditView(views.UpdateView):
    model = Photo  # or queryset  - because must have self.object
    form_class = PhotoEditForm
    template_name = "photos/photo-edit-page.html"
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse_lazy('photo_details',
                            kwargs={"pk": self.object.pk})


def photo_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    return redirect('home')

class PhotoDeleteView(views.DeleteView):
    model = Photo
    fields = '__all__'
    # TODO
    success_url = reverse_lazy('home')


