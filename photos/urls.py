from django.urls import path, include

from common.views import AddCommentView
from photos.views import  CreatePhotoView, PhotoDetailsView, PhotoEditView, PhotoDeleteView

urlpatterns = [
    path('add/', CreatePhotoView.as_view(), name='add_photo'),
    path('<int:pk>/',
         include([
             path('', PhotoDetailsView.as_view(), name='photo_details'),
             path('edit/', PhotoEditView.as_view(), name='photo_edit'),
             path('delete/', PhotoDeleteView.as_view(), name='photo_delete'),
             path('comment/',AddCommentView.as_view(), name='add comment')
         ])),
]
