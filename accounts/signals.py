import logging
from datetime import datetime

from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save
from django.dispatch import receiver

from Petstagram2024 import settings

from .models import Profile

# !!!!!!!!!!!
# 'def ready(self)' in apps.py to work signals
# in settings InstalledApps - to be declared with accounts.apps.AccountConfig

# created - True if just created, False if updated
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)  # instance=email (username)


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    logging.info(f" {user} logged-in  at {datetime.now()}")


@receiver(user_logged_out)
def log_user_login(sender, request, user, **kwargs):
    logging.info(f" {user} logged-out  at {datetime.now()}")
