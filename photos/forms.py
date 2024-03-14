from photos.models import Photo
from django import forms


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('date_time_of_publication', 'user')

        labels = {
            'photo': 'Photo file',
            'tagged_pets': 'Tag pets',
        }


class PhotoEditForm(PhotoForm):
    class Meta:
        model = Photo
        exclude = ('photo','date_time_of_publication', 'user')
