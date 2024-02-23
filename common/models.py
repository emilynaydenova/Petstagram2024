from django.db import models

from photos.models import Photo


class Comment(models.Model):
    COMMENT_MAX_LENGTH = 300

    text = models.TextField(
        max_length=COMMENT_MAX_LENGTH,
    )

    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT
    )

    # user = models.ForeignKey(User)

    def __str__(self):
        return self.to_photo.location

    class Meta:
        ordering = ["date_time_of_publication"]


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT
    )


    # user = models.ForeignKey(User)

# like = Like.objects.filter(photo_id=pet_photo.pk,user=request.user)
