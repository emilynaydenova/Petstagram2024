from django.urls import path

from common.views import IndexView

urlpatterns = [
    # path('', index, name='home'),
    path("", IndexView.as_view(), name="home"),
]
