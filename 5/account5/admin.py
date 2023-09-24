from django.contrib import admin
from .models import CustomUser5
from django.contrib.auth.admin import UserAdmin
from polls5.forms import NewsForm5

# Register your models here.\

class NewsAdmin(admin.ModelAdmin):
    form = NewsForm5
    list_display = ("title", 'body')
    search_fields = ("title", "body")


class CustomUserAdmin(UserAdmin):
    model = CustomUser5
    list_display = ("username", "is_staff", "is_active","roles")
    list_filter = ("username", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions", "roles"
            )}
         ),
    )
    search_fields = ("username",)
    ordering = ("username",)




admin.site.register((CustomUser5), CustomUserAdmin)