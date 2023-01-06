"""
User's app forms.
"""
from django import forms
from django.contrib.auth import get_user_model


class RegisterForm(forms.ModelForm):
    """Register new user's form."""

    class Meta:
        model = get_user_model()
        fields = [
            'name', 'username',
            'email', 'password'
        ]

    def clean(self):
        pass
