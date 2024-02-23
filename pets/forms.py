from django import forms
from django.core.exceptions import ValidationError

from core.form_mixins import ReadonlyDisabledFieldsMixin
from pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "date_of_birth", "pet_photo"]

        labels = {
            "name": "Pet name",
            "date_of_birth": "Date of birth",
            "pet_photo": "Link to image",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={'placeholder': "Pet name"}),
            "date_of_birth": forms.DateInput(
                attrs={'type': 'date'}),
            "pet_photo": forms.URLInput(
                attrs={'placeholder': "Link to image"}),
        }


class PetEditForm(PetForm, ReadonlyDisabledFieldsMixin):
    readonly_fields = ('date_of_birth',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].label = "DoB Read Only"
        self._mark_readonly_fields()
        # can use mixin instead of
        # self.fields['date_of_birth'].widget.attrs["readonly"] = True


    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth != self.instance.date_of_birth:
            raise ValidationError("DoB is readonly")
        return self.instance.date_of_birth
        # if date_of_birth:
        #     begin_date = date(1950, 1, 1)
        #     end_date = date.today()
        #     if date_of_birth < begin_date or date_of_birth > end_date:
        #         raise ValidationError(
        #             f"Date must be between {begin_date.day}.{begin_date.month}.{begin_date.year} and today.")
        # return date_of_birth


class PetDeleteForm(PetForm, ReadonlyDisabledFieldsMixin):
    disabled_fields = ('name', 'date_of_birth', 'pet_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._mark_disabled_fields()

