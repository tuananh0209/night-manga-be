from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.utils.translation import gettext_lazy as _

from core.admin import StaffAdmin
from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import User
from core.utils import encrypt_image, decrypt_image

class UserAdmin(AuthUserAdmin, StaffAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "avatar",
                    "is_staff",
                    "is_superuser",
                    "is_active",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )
    list_display = (
        "email",
        "username"
    )
    search_fields = ("email", "username")
    ordering = ("-date_joined",)
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        "groups",
    )

    def get_queryset(self, request):
        return super().get_queryset(request)

    def has_add_permission(self, request):
        return True

    def save_model(self, request, obj, form, change):
        if obj.email == "":
            obj.email = None
        super().save_model(request, obj, form, change)
        # decrypt_image(path=obj.avatar.path) 
        # encrypt_image(path=obj.avatar.path)
           
        if obj.avatar and change and 'avatar' in form.changed_data:
            avatar = obj.avatar
            if avatar:
                encrypt_image(path=avatar.path)

    def delete_model(self, request, obj):
        return super().delete_model(request, obj)

    def delete_queryset(self, request, queryset):
        return super().delete_queryset(request, queryset)


admin.site.register(User, UserAdmin)
