from django import template
#
# from profiles.models import Profile
#
# register = template.Library()
#
# # for using in base.html
# @register.simple_tag()
# def has_profile():
#     profiles_count = Profile.objects.count()
#     return profiles_count > 0
#
#
# @register.simple_tag()
# def profile_pk():
#     profile = Profile.objects.first()
#     if profile:
#         return profile.pk
