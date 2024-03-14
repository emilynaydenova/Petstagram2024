

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from Petstagram2024 import settings
from accounts.managers import CustomUserManager

# from accounts.validators import ValidateFileMaxSizeInMb
"""" 
!!! if you are building an app with user authentication,
you should consider creating a custom user model at the beginning
of the work process.

1. Create model extending User model. -> CustomUser
2. Configure model in settings -> AUTH_USER_MODEL = 'accounts.CustomUser'
3. Create user manager for our model -> managers.py
"""


 # Look at AbstractUser
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists.")
        }
    )
    # password comes from AbstractBaseUser
    # last_login comes from AbstractBaseUser

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    # is_superuser comes from PermissionsMixin

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    # groups come from PermissionsMixin
    # user_permissions come from PermissionsMixin
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    # says to AbstractBaseUser how to identify the user
    USERNAME_FIELD = "email"
    # EMAIL_FIELD = "email"
    # REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def get_profile(self):
        profile = Profile.objects.filter(pk=self.id)[0]
        return profile

    @property
    def get_email_username(self):
        name = self.email.split('@')[0] or None
        return name

    class Meta:
        verbose_name = "User"


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    MAX_LENGTH_GENDER = 20

    class GENDER(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
        DO_NOT_SHOW = 'do_not_show', 'gender-no selection'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,  # user and profile will have the same pk
        on_delete=models.CASCADE,  # make CustomUser.is_active = False

    )  # can access through profile_obj.pk or profile_obj.user_id

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    gender = models.CharField(
        max_length=MAX_LENGTH_GENDER,
        choices=GENDER.choices,
        default=GENDER.DO_NOT_SHOW,
    )


    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.first_name or self.last_name

    def __str__(self):
        return self.full_name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #     img.thumbnail(output_size)
    #     img.save(self.image)
