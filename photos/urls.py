from django.urls import path, include

from photos.views import CreatePhotoView, PhotoDetailsView, PhotoEditView, PhotoDeleteView, AddCommentView, like_photo

urlpatterns = [
    path('add/', CreatePhotoView.as_view(), name='add_photo'),
    path('<int:pk>/',
         include([
             path('', PhotoDetailsView.as_view(), name='photo_details'),
             path('edit/', PhotoEditView.as_view(), name='photo_edit'),
             path('delete/', PhotoDeleteView.as_view(), name='photo_delete'),
             path('like/', like_photo, name='like_photo'),
             path('comment/',AddCommentView.as_view(), name='add comment')
         ])),
]
