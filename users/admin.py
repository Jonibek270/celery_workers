from django.contrib import admin

from .models import UserOTP, CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_active", 'username', "is_superuser")


@admin.register(UserOTP)
class UserOtpAdmin(admin.ModelAdmin):
    list_display = ('user','otp', 'created_at', 'is_used',)
# Register your models here.
