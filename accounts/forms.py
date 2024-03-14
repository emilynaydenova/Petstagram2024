from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile

UserModel = get_user_model()


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email",)
        # password1 and password2 come from UserCreationForm

        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email",
                    "autofocus": True,
                })}

    # password1 and password2 are declared on the UserCreationForm
    # (they aren't model fields), therefore you can't use them in widgets.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].help_text = None
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
                # "title": "Not less than 8 symbols",
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Repeat password",

            }
        )


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Password",

            }
        )
        #  username instead of email
        self.fields["username"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Email",
                "autofocus": True,
            }
        )

        # self.fields['password'].label = "Password"

    class Meta:
        model = UserModel
        fields = ("email",)
        # username and password come from AuthenticationForm


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user",)  # it is a FK

        widgets = {
            "image": forms.FileInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "first name",
                    "autofocus": True,
                    "title": "First name",
                },
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "last name",
                    "title": "Last name",
                },
            ),
        }


# used in Django admin Custom User creation


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user",)  # it is a FK


# for admin - change user
class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = (
            "email",
            "password",
            "is_staff",
            "is_superuser",
        )
