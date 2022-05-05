from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import OurticleUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = OurticleUser
        fields = ('username','email','age',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = OurticleUser
        fields = ('username','email','age',)