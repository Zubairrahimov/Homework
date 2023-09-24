from django.contrib import admin
from .models import CustomUser3
from django.contrib.auth.admin import UserAdmin
from polls3.forms import NewsForm3
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser3
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

class NewsAdmin(admin.ModelAdmin):
    form = NewsForm3
    list_display = ("title", 'body')
    search_fields = ("title", "body")


admin.site.register((CustomUser3), CustomUserAdmin)