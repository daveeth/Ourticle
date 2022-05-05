from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import OurticleUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = OurticleUser
    list_display = ['username', 'email','age', 'is_staff']

admin.site.register(OurticleUser, CustomUserAdmin)




