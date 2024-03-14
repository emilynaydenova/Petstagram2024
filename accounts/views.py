from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin

from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from accounts.forms import (
    RegisterUserForm,
    LoginUserForm,
    EditProfileForm,
    DeleteProfileForm, UserModel,
)
from accounts.models import Profile
from common.models import Like
from pets.models import Pet
from photos.models import Photo


class OwnerRequiredMixin(LoginRequiredMixin, AccessMixin):
    """ Verify that the current user has this profile"""

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs.get('pk', None):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)





# LoginRequiredMixin is used
class LoginUserView(LoginView):
    template_name = "accounts/login-page.html"
    form_class = LoginUserForm
    redirect_authenticated_user = True  # prevent login site again if is logged

    # LOGIN_REDIRECT_URL = reverse_lazy('home') in settings


class RegisterUserView(CreateView):
    template_name = "accounts/register-page.html"
    form_class = RegisterUserForm
    redirect_authenticated_user = True  # prevent auth.user from this page
    success_url = reverse_lazy("home")

    # it is called after success
    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        user = self.object  # or form.instance
        login(self.request, user)
        return result


# make form and use Post method +csrf_token to logout
# the session data for the current request is completely cleaned out
# class LogoutUserView(LogoutView):
#    template_name = 'accounts/logout.html'

# def dispatch(self, request, *args, **kwargs):
#     if request.method == 'GET':
#         # Perform logout action for GET request
#         logout(request)
#         return redirect('home')
#     return super().dispatch(request, *args, **kwargs)


class DetailProfileView(OwnerRequiredMixin, DetailView):
    queryset = Profile.objects.all()
    template_name = 'accounts/profile-details-page.html'
    context_object_name = 'profile'

    def get_object(self, *args, **kwargs):
        # load data or empty
        profile = Profile.objects.filter(pk=self.kwargs["pk"]).first()
        if not profile:
            profile = Profile.objects.create(pk=self.kwargs["pk"])
        return profile

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        pets = Pet.objects.filter(user=self.request.user.pk)
        photos = Photo.objects.filter(user=self.request.user.pk)
        likes = Like.objects.filter(user=self.request.user.pk)
        context = {
             'pets': pets,
             'photos': photos,
             'profile': self.get_object(),
             'likes': likes,
        }
        return context


class EditProfileView(OwnerRequiredMixin, UpdateView):
    model = Profile
    exclude = ("user",)
    form_class = EditProfileForm
    template_name = "accounts/profile-edit-page.html"

    def get_success_url(self):
        return reverse_lazy("profile_show", kwargs={'pk': self.object.pk})

    def get_object(self, *args, **kwargs):
        # load data or empty
        profile = get_object_or_404(Profile, pk=self.kwargs["pk"])
        return profile


class DeleteProfileView(OwnerRequiredMixin, DeleteView):
    model = Profile
    exclude = ("user",)
    form_class = DeleteProfileForm
    template_name = "accounts/profile-delete-page.html"
    success_url = reverse_lazy("home")

    def get_object(self, *args, **kwargs):
        # load data or empty
        profile = get_object_or_404(Profile, pk=self.kwargs["pk"])
        return profile
