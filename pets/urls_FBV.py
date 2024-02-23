from django.urls import path, include

from pets.views_FBV import add_pet, pet_details, pet_edit, pet_delete

urlpatterns = [
    path('add/', add_pet, name='add_pet'),
    path('<str:username>/pet/<slug:pet_slug>/',
         include([
             path('', pet_details, name='pet_details'),
             path('edit/', pet_edit, name='pet_edit'),
             path('delete/', pet_delete, name='pet_delete')
         ]))
]
