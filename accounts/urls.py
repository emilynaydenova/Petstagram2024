
from django.urls import path, include

from accounts.views import (register, show_profile,
                            edit_profile, delete_profile, logout_view, login_view)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login_user'),
    path("logout/", logout_view, name="logout_user"),
    path('profile/<int:pk>/',
         include([
             path('', show_profile, name='profile_show'),
             path('edit/', edit_profile, name='profile_edit'),
             path('delete/', delete_profile, name='profile_delete')
         ])),
]
