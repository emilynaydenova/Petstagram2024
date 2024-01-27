from django.shortcuts import render


# Create your views here.
def add_pet(request):
    context = {}
    return render(request, "pets/pet-add-page.html", context)


def pet_details(request, username, pet_slug):
    context = {}
    return render(request, "pets/pet-details-page.html", context)


def pet_edit(request, username, pet_slug):
    context = {}
    return render(request, "pets/pet-edit-page.html", context)


def pet_delete(request, username, pet_slug):
    context = {}
    return render(request, "pets/pet-delete-page.html", context)
