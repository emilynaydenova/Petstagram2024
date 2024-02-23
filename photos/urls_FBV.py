from django.urls import path, include

from photos.views import add_photo, photo_details, photo_edit, photo_delete

urlpatterns = [
    path('add/', add_photo, name='add_photo'),
    path('<int:pk>/',
         include([
             path('', photo_details, name='photo_details'),
             path('edit/', photo_edit, name='photo_edit'),
             path('delete/', photo_delete, name='photo_delete'),
         ])),
]
