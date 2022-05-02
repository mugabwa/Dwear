from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields':['email', 'first_name',
        'last_name']}),
        ('User Login Information', {'fields': ['is_staff', 'is_active',
        'password', 'date_joined']}),
    ]

admin.site.register(CustomUser, CustomUserAdmin)