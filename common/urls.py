from django.urls import path

from common.views import  like_photo, IndexView

urlpatterns = [
    # path('', index, name='home'),
    path("",IndexView.as_view(),name="home"),
    path('photo_like/<int:pk>/', like_photo, name='like_photo'),
]
