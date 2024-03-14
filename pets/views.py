from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from common.forms import CommentForm
from pets.forms import PetForm, PetEditForm, PetDeleteForm
from pets.models import Pet
from photos.models import Photo



class PetCreateView(LoginRequiredMixin,views.CreateView):
    # can use model + fields if you create a form by modelform_factory
    # model = Pet
    # fields='__all__'
    # else -> only form_class

    form_class = PetForm
    template_name = "pets/pet-add-page.html"  # default is "pets/pet_form.html
    context_object_name = "pet"

    # save pet with FK-user after filling form
    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        return super().form_valid(form)

    # or fill user before filling form
    def get_form(self,form_class=None):
        form = super().get_form(form_class=form_class)
        form.instance.user = self.request.user
        return form

    def get_success_url(self):
        # self.object comes from form.save() in PetForm
        username = self.request.user.email.split('@')[0] or None
        return reverse_lazy("pet_details",
                            kwargs={"username": username,
                                    "pet_slug": self.object.slug,
                                    })
    # def get_success_url(self):
    #     return reverse_lazy('profile_show', kwargs={'pk': self.request.user.pk})

    # def get_success_url(self):
    #     # Get the referring page URL
    #     referring_page = self.request.META.get('HTTP_REFERER')
    #
    #     # If the referring page exists and is not the current page,
    #     # return it as the success URL
    #     if referring_page and referring_page != self.request.path:
    #         return referring_page
    #
    #     # If the referring page is not available or is the current page,
    #     # return a default URL
    #     return reverse_lazy('home')  # Change 'index' to the name of your default URL pattern

class PetDetailsView(LoginRequiredMixin,views.DetailView):
    model = Pet  # or queryset
    template_name = "pets/pet-details-page.html"
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'  # name in URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['photos_count'] = self.object.photo_set.count()
        context['comment_form'] = CommentForm()
        return context


class PetEditView(LoginRequiredMixin,views.UpdateView):
    # model = Pet  # or queryset=Pet.objects.all()  - because must have self.object
    queryset = Pet.objects.all() \
        .prefetch_related('photo_set') \
        .prefetch_related('photo_set__like_set') \
        .prefetch_related('photo_set__tagged_pets')

    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'

    # to permit edition only to the owner
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not self.request.user.is_authenticated or obj.user != self.request.user:
            return self.handle_no_permission()
        return obj

    def get_success_url(self):
        # self.object comes from form.save() in PetForm
        return reverse_lazy("pet_details",
                            kwargs={"username": self.kwargs['username'],
                                    "pet_slug": self.kwargs['pet_slug'],
                                    })


class PetDeleteView(LoginRequiredMixin,views.DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = "pets/pet-delete-page.html"
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'
    success_url = reverse_lazy('home')

    # to fill delete form with instance data
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        self.object.delete()
        return redirect(self.success_url)
