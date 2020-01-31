from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    """ Custom user Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
    list_filter = UserAdmin.list_filter + ("superhost",)
