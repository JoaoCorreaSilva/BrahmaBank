from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm
)

from .models import *

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'registro',
    ]
    fieldsets = [
        [
            None,
            {
                'fields': [
                    'password'
                ]
            }
        ],
        [
            'Personal Information',
            {
                'fields': [
                    'foto',
                ]
            }
        ],
        [
            'Permissions',
            {
                'fields': [
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions'
                ]
            }
        ],
        [
            'Important Dates',
            {
                'fields': [
                    'last_login',
                    'date_joined'
                ]
            }
        ]
    ]
