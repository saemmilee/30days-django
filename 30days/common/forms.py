from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from common.models import profile


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = profile
        fields = ['RMR', 'RC', 'exercise']