from django.urls import path, include

from pets.views import PetCreateView, PetDetailsView, PetEditView, PetDeleteView
from pets.views_FBV import pet_details, pet_edit, pet_delete

urlpatterns = [
    path('add/', PetCreateView.as_view(), name='add_pet'),
    path('<str:username>/pet/<slug:pet_slug>/',
         include([
             path('', PetDetailsView.as_view(), name='pet_details'),
             path('edit/', PetEditView.as_view(), name='pet_edit'),
             path('delete/', PetDeleteView.as_view(), name='pet_delete')
         ]))
]
