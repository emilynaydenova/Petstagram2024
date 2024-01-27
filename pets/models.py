from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):
    NAME_MAX_LENGTH = 30

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    pet_photo = models.URLField()

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    # autogenerated -> change save()
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
        editable=False,  # readonly,hidden in Django admin
    )

    def save(self, *args, **kwargs):
        # first save is for generate id, and to use then in the slug
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.pk}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


"""
slugify(value):

Convert to ASCII. Convert spaces to hyphens. 
Remove characters that aren't alphanumerics,
underscores, or hyphens.
Convert to lowercase. Also strip
leading and trailing whitespace.
"""