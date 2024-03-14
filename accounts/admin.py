from django.contrib import admin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterUserForm
from .models import Profile

UserModel = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ("first_name", "last_name",)
    verbose_name_plural = "Profile"
    fk_name = "user"


# can change user via django admin
@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    # used custom UserCreateForm so password would be hashed
    add_form = RegisterUserForm
    inlines = (ProfileInline,)

    list_display = (
        "pk",
        "email",
        "is_staff",
        "is_superuser",
    )

    list_select_related = ("profile",)
    search_fields = ("email",)
    ordering = ("pk",)

    fieldsets = (
        (
            None,
            {
                "fields": ("email","password"),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                    "is_active",

                ),
            },
        ),
    )

    def get_inline_instances(self, request, obj=None):
        """to display the inlines only in the edit form."""
        if not obj:
            return list()
        return super(UserModelAdmin, self).get_inline_instances(request, obj)

    def get_groups(self, obj):
        return obj.groups.values_list("name", flat=True).get()

    get_groups.short_description = "Groups"

