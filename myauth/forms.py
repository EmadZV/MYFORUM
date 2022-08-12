from django import forms
from .models import UserModel


class LogInForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password')
