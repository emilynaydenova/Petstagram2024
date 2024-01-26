from django.urls import path

from photos.views import add_photo, photo_details, photo_edit

urlpatterns = [
    path('add',add_photo,name='add photo'),
    path('<int:pk>',photo_details),
    path('<int:pk>/edit/',photo_edit),
]