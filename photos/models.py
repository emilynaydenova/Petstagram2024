from django.core.validators import MinLengthValidator
from django.db import models

from pets.models import Pet
from photos.validators import ValidateFileMaxSizeInMb


class Photo(models.Model):
    IMAGE_MAX_SIZE_MB = 5
    DESCRIPTION_MIN_LENGTH = 10
    DESCRIPTION_MAX_LENGTH = 300
    LOCATION_MAX_LENGTH = 30

    photo = models.ImageField(
        "Pet photo",
        upload_to="pet_photos/",  # The location of the uploaded image will be in MEDIA_ROOT/images

        validators=[
            ValidateFileMaxSizeInMb(
                max_size=IMAGE_MAX_SIZE_MB,
            )],
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        blank=True,
        null=True,
        validators=(
            MinLengthValidator(DESCRIPTION_MIN_LENGTH),),
    )

    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        blank=True,
        null=True)

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True)

    date_of_publication = models.DateField(auto_now=True)


class Comment(models.Model):
    COMMENT_MAX_LENGTH = 30

    text = models.TextField(
        max_length=COMMENT_MAX_LENGTH,
    )

    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.DO_NOTHING
    )

    # user = models.ForeignKey(User)


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.DO_NOTHING
    )

    # user = models.ForeignKey(User)