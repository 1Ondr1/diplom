from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Додаткові поля', {'fields': ('avatar',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Додаткові поля', {'fields': ('avatar',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
