from django.shortcuts import render, redirect

from common.models import Like
from photos.models import Photo
from django.views import generic as views

# Create your views here.
def index(request):
    pet_name_pattern = request.GET.get('pet_name_pattern','').strip()

    photos = Photo.objects.all()

    if pet_name_pattern:
        photos = photos.filter(tagged_pets__name__icontains=pet_name_pattern)

    context = {
        "photos": photos,
        "pet_name_pattern": pet_name_pattern,
    }
    return render(request, 'common/home-page.html', context)


# pk of the photo
def like_photo(request, pk):
    photo_like = Like.objects.filter(to_photo_id=pk).first()  # ,user=request.user)
    if photo_like:
        # dislike
        photo_like.delete()
    else:
        Like.objects.create(to_photo_id=pk)
    return redirect(request.META['HTTP_REFERER'] + f'#photo-{pk}')
