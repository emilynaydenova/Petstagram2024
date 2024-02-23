from django.shortcuts import render, redirect, get_object_or_404

from pets.forms import PetForm, PetEditForm, PetDeleteForm
from pets.models import Pet
from photos.models import Photo


# Create your views here.
def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        pet = form.save()
        return redirect('pet_details', username=request.user.username, pet_slug=pet.slug)

    context = {
        'form': form,
    }
    return render(request, "pets/pet-add-page.html", context)


# Use get_object_or_404 instead of get to handle cases
# where the pet with the given slug does not exist.
def pet_edit(request, username, pet_slug):
    pet = get_object_or_404(Pet, slug=pet_slug)

    if request.method == 'POST':
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()

            return redirect('pet_details', username=request.user.username, pet_slug=pet.slug)
    else:
        form = PetEditForm(instance=pet)

    context = {
        'form': form,
        'pet': pet,
    }
    return render(request, "pets/pet-edit-page.html", context)


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    context = {
        'pet': pet,
        'photos': Photo.objects.count(),
    }
    return render(request, "pets/pet-details-page.html", context)


def pet_delete(request, username, pet_slug):
    pet = get_object_or_404(Pet, slug=pet_slug)
    form = PetDeleteForm(request.POST or None, instance=pet)
    if request.method == 'POST':
        # pet.delete()
        form.save()   # save is overwritten in PetDeleteForm to delete instance
        return redirect('home')

    context = {
        "form": form,
        "pet": pet,
    }
    return render(request, "pets/pet-delete-page.html", context)
