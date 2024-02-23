from django.contrib import admin

from photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "pk", "date_of_publication", "short_description",
        "get_tagged_pets")

    @staticmethod
    def short_description(obj):
        return f'{obj.description[:20]} ...'

    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join([pet.name for pet in obj.tagged_pets.all()])

    # @staticmethod
    # def get_thumbnail(obj):
    #     return "<img src="f'{obj.photo.url}'">{}</a>"

    # def link_to_pet(self,obj):
    #     return f'<a href="/">{obj.name}</a> '

