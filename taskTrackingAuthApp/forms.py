from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class AccountCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "user_role"]


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "email"]

        extra_kwargs = {
            "password": {"required": False}
        }
