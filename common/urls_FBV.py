from django.urls import path

from common.views_FBV import index, like_photo

urlpatterns = [
    path('', index, name='home'),
    path('photo_like/<int:pk>/', like_photo, name='like_photo'),
]
