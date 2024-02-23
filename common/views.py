from django.shortcuts import render, redirect

from common.models import Like, Comment
from photos.models import Photo
from django.views import generic as views


#
class IndexView(views.ListView):
    # Join to Pet and Like for downing of SELECT
    queryset = Photo.objects.all() \
        .prefetch_related('tagged_pets') \
        .prefetch_related("like_set")
    template_name = 'common/home-page.html'
    context_object_name = 'photos'

    paginate_by = 1   # <- ->
    # or def get_paginate_by(self,queryset)
    @property
    def pet_name_pattern(self):
        return self.request.GET.get('pet_name_pattern', '').strip()

    def get_queryset(self):
        queryset = super().get_queryset()

        # if self.pet_name_pattern:
        #     queryset = queryset.filter(tagged_pets__name__icontains=pet_name_pattern)

        # for many filters
        filter_query = {}
        if self.pet_name_pattern:
            filter_query['tagged_pets__name__icontains'] = self.pet_name_pattern
        queryset = queryset.filter(**filter_query)

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pet_name_pattern'] = self.pet_name_pattern
        return context


# pk of the photo
def like_photo(request, pk):
    photo_like = Like.objects.filter(to_photo_id=pk).first()  # ,user=request.user)
    if photo_like:
        # dislike
        photo_like.delete()
    else:
        Like.objects.create(to_photo_id=pk)
    return redirect(request.META['HTTP_REFERER'] + f'#photo-{pk}')

class AddCommentView(views.CreateView):
    model = Comment
