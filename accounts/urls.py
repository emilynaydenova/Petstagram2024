from django.contrib.auth.views import LogoutView
from django.urls import path, include

from accounts.views import RegisterUserView, LoginUserView, DetailProfileView, EditProfileView, \
    DeleteProfileView

urlpatterns = [
    path('register/',RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path("logout/", LogoutView.as_view(), name="logout_user"),
    path('profile/<int:pk>/',
         include([
             path('', DetailProfileView.as_view(), name='profile_show'),
             path('edit/', EditProfileView.as_view(), name='profile_edit'),
             path('delete/', DeleteProfileView.as_view(), name='profile_delete')
         ])),
]
