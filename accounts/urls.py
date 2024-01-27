from django.contrib.auth.views import LogoutView
from django.urls import path, include

from accounts.views import register, login, show_profile, edit_profile, delete_profile, logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path("logout/",  logout, name="logout"),
    path('profile/<int:pk>/',
         include([
             path('', show_profile, name='profile_show'),
             path('edit/', edit_profile, name='profile_edit'),
             path('delete/', delete_profile, name='profile_delete')
         ])),
]
