from django.contrib import admin

from pets.models import Pet


# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
     # inlines = (PhotosInline,)
    list_display = (
        "name", "date_of_birth",
        "slug",
    )
    verbose_name_plural = "Pets"
    ordering = ("name",)
