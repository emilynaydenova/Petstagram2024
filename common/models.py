from django.contrib.auth import get_user_model
from django.db import models

from photos.models import Photo

UserModel = get_user_model()


class Comment(models.Model):
    COMMENT_MAX_LENGTH = 300

    text = models.TextField(
        max_length=COMMENT_MAX_LENGTH,
    )

    date_time_of_publication = models.DateTimeField(auto_now_add=True)

    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    ) # RESTRICT prevent deletion of UserModel
    # if there are still related objects depending on it.

    def __str__(self):
        return self.to_photo.location

    class Meta:
        ordering = ["date_time_of_publication"]


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

# like = Like.objects.filter(photo_id=pet_photo.pk,user=request.user)
